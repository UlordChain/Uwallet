import ast
import os

import jsonrpclib
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCRequestHandler, SimpleJSONRPCServer

from uwallet.commands import Commands, known_commands
from uwallet.simple_config import SimpleConfig
from uwallet.util import DaemonThread, json_decode
from uwallet.wallet import Wallet, WalletStorage


def lockfile(config):
    return os.path.join(config.path, 'daemon')


def get_daemon(config):
    try:
        with open(lockfile(config)) as f:
            host, port = ast.literal_eval(f.read())
    except:
        return
    server = jsonrpclib.Server('http://%s:%d' % (host, port))
    # check if daemon is running
    try:
        server.ping()
        return server
    except:
        pass


class RequestHandler(SimpleJSONRPCRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def end_headers(self):
        self.send_header("Access-Control-Allow-Headers",
                         "Origin, X-Requested-With, Content-Type, Accept")
        self.send_header("Access-Control-Allow-Origin", "*")
        SimpleJSONRPCRequestHandler.end_headers(self)


class Daemon(DaemonThread):
    def __init__(self, config, network):
        DaemonThread.__init__(self)
        self.config = config
        self.network = network
        self.wallets = {}
        self.wallet = self.load_wallet(config.get_wallet_path())
        self.cmd_runner = Commands(self.config, self.wallet, self.network)
        host = config.get('rpchost', 'localhost')
        port = config.get('rpcport', 0)
        self.server = SimpleJSONRPCServer((host, port), requestHandler=RequestHandler,
                                          logRequests=False)
        with open(lockfile(config), 'w') as f:
            f.write(repr(self.server.socket.getsockname()))
        self.server.timeout = 0.1
        for cmdname in known_commands:
            self.server.register_function(getattr(self.cmd_runner, cmdname), cmdname)
        self.server.register_function(self.run_cmdline, 'run_cmdline')
        self.server.register_function(self.ping, 'ping')
        self.server.register_function(self.run_daemon, 'daemon')

    def ping(self):
        return True

    def run_daemon(self, config):
        sub = config.get('subcommand')
        assert sub in ['start', 'stop', 'status']
        if sub == 'start':
            response = "Daemon already running"
        elif sub == 'status':
            p = self.network.get_parameters()
            response = {
                'path': self.network.config.path,
                'server': p[0],
                'blockchain_height': self.network.get_local_height(),
                'server_height': self.network.get_server_height(),
                'nodes': self.network.get_interfaces(),
                'connected': self.network.is_connected(),
                'auto_connect': p[3],
                'wallets': dict([(k, w.is_up_to_date()) for k, w in self.wallets.items()]),
            }
        elif sub == 'stop':
            self.stop()
            response = "Daemon stopped"
        return response

    def load_wallet(self, path, get_wizard=None):
        if path in self.wallets:
            wallet = self.wallets[path]
        else:
            storage = WalletStorage(path)
            if get_wizard:
                if storage.file_exists:
                    wallet = Wallet(storage)
                    action = wallet.get_action()
                else:
                    action = 'new'
                if action:
                    wizard = get_wizard()
                    wallet = wizard.run(self.network, storage)
                else:
                    wallet.start_threads(self.network)
            else:
                wallet = Wallet(storage)
                # automatically generate wallet for unet
                if not storage.file_exists:
                    seed = wallet.make_seed()
                    wallet.add_seed(seed, None)
                    wallet.create_master_keys(None)
                    wallet.create_main_account()
                    wallet.synchronize()

                wallet.start_threads(self.network)
            if wallet:
                self.wallets[path] = wallet
        return wallet

    def run_cmdline(self, config_options):
        config = SimpleConfig(config_options)
        cmdname = config.get('cmd')
        cmd = known_commands[cmdname]
        path = config.get_wallet_path()
        wallet = self.load_wallet(path) if cmd.requires_wallet else None
        # arguments passed to function
        args = map(lambda x: config.get(x), cmd.params)
        # decode json arguments
        args = map(json_decode, args)
        # options
        args += map(lambda x: config.get(x), cmd.options)
        cmd_runner = Commands(config, wallet, self.network,
                              password=config_options.get('password'),
                              new_password=config_options.get('new_password'))
        func = getattr(cmd_runner, cmd.name)
        result = func(*args)
        return result

    def run(self):
        while self.is_running():
            self.server.handle_request()
        os.unlink(lockfile(self.config))

    def stop(self):
        for k, wallet in self.wallets.items():
            wallet.stop_threads()
        DaemonThread.stop(self)
