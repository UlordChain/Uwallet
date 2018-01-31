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
HEADER_SIZE = 112
BLOCKS_PER_CHUNK = 96   #1d / 150s

HEADERS_URL = "" #TODO add

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
        'pubkey_address_prefix': 68,   #85
        'script_address_prefix': 16,   #122 204
        'genesis_hash': '000002287d4bdfb69539d264be0eae5f08c8f990732b84cb6c0834bcee80de3a',
        'max_target': 0x0007FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        'genesis_bits': 0x1e0ffff0,      #0x1f00ffff
        'target_timespan': 150           #150
    }
}
 