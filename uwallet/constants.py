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
        'pubkey_address_prefix': 36,   #85
        'script_address_prefix': 16,   #122 204
        'genesis_hash': '000002287d4bdfb69539d264be0eae5f08c8f990732b84cb6c0834bcee80de3a',
        'max_target': 0x0007FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        'genesis_bits': 0x1f07ffff,      #0x1f00ffff
        'target_timespan': 150           #150
    },
    'unet_test': {
        'pubkey_address': 0,
        'script_address': 5,
        'pubkey_address_prefix': 66,    #changed
        'script_address_prefix': 239,   #196,
        'genesis_hash': '04994b3eaeed96e070107823dfa796d5d45246e72ed838054780b4e6de455971',
        'max_target': 0x07FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        'genesis_bits': 0x2007ffff,     #0x1f00ffff
        'target_timespan': 150
    },
    'unet_regtest': {
        'pubkey_address': 0,
        'script_address': 5,
        'pubkey_address_prefix': 34,
        'script_address_prefix': 239,
        'genesis_hash': '01c8d71dc9be94898366fa035561a8b58b2ca9a78f2ce9601ef07038e13d54ff',
        'max_target': 0x0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F,     
        'genesis_bits': 0x200f0f0f,
        'target_timespan': 150          #150? should be less
    }
}
 