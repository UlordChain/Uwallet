RECOMMENDED_FEE = 50000
COINBASE_MATURITY = 100
COIN = 100000000

# supported types of transaction outputs
TYPE_ADDRESS = 1
TYPE_PUBKEY = 2
TYPE_SCRIPT = 4
TYPE_CLAIM = 8
TYPE_SUPPORT = 16
TYPE_UPDATE = 32

# claim related constants
EXPIRATION_BLOCKS = 262974
RECOMMENDED_CLAIMTRIE_HASH_CONFIRMS = 1

NO_SIGNATURE = 'ff'

NULL_HASH = '0000000000000000000000000000000000000000000000000000000000000000'
HEADER_SIZE = 140
BLOCKS_PER_CHUNK = 96   #1d / 150s

#TODO add it. --JustinQP
HEADERS_URL = "" 

DEFAULT_PORTS = {'t': '10579', 's': '50002', 'h': '8081', 'g': '8082'}
NODES_RETRY_INTERVAL = 60
SERVER_RETRY_INTERVAL = 10
MAX_BATCH_QUERY_SIZE = 500
proxy_modes = ['socks4', 'socks5', 'http']

# Main network and testnet3 definitions
# these values follow the parameters in unet/src/chainparams.cpp
blockchain_params = {
    'unet_main': {
        'pubkey_address': 0,
        'script_address': 5,
        'pubkey_address_prefix': 68,
        'script_address_prefix': 63,
        'genesis_hash': '000000e32e974118821c865e0f79cd851edd96ccdf161de997ee85c438d0e7e3',
        'max_target': 0x00001d1459000000000000000000000000000000000000000000000000000000,
        'genesis_bits': 0x1e1d1459,
        'target_timespan': 150 
    },
    'unet_test': {
        'pubkey_address': 0,
        'script_address': 5,
        'pubkey_address_prefix': 130,
        'script_address_prefix': 125,
        'genesis_hash': '04994b3eaeed96e070107823dfa796d5d45246e72ed838054780b4e6de455971',
        'max_target': 0x07FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        'genesis_bits': 0x2007ffff,
        'target_timespan': 150
    },
    'unet_regtest': {
        'pubkey_address': 0,
        'script_address': 5,
        'pubkey_address_prefix': 140,
        'script_address_prefix': 120,
        'genesis_hash': '0158f211e2881c0e725fcc6ec25db2b72ad4a3f8f7830a516e9d6570e9527fd1',
        'max_target': 0x0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F,     
        'genesis_bits': 0x200f0f0f,
        'target_timespan': 150
    }
}