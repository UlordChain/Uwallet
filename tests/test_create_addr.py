import hashlib
import hmac

__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def sha256(x):
    return hashlib.sha256(x).digest()


def sha512(x):
    return hashlib.sha512(x).digest()


def ripemd160(x):
    h = hashlib.new('ripemd160')
    h.update(x)
    return h.digest()


def Hash(x):
    if type(x) is unicode:
        x = x.encode('utf-8')
    return sha256(sha256(x))


def hash_160(public_key):
    md = hashlib.new('ripemd160')
    md.update(sha256(public_key))
    return md.digest()

def base_encode(v, base):
    """ encode v, which is a string of bytes, to base58."""
    if base == 58:
        chars = __b58chars
    long_value = 0L
    for (i, c) in enumerate(v[::-1]):
        long_value += (256 ** i) * ord(c)
    result = ''
    while long_value >= base:
        div, mod = divmod(long_value, base)
        result = chars[mod] + result
        long_value = div
    result = chars[long_value] + result
    # Bitcoin does a little leading-zero-compression:
    # leading 0-bytes in the input become leading-1s
    nPad = 0
    for c in v:
        if c == '\0':
            nPad += 1
        else:
            break
    return (chars[0] * nPad) + result


def hash_160_to_bc_address(h160):
    c = chr(36)
    vh160 = c + h160
    h = Hash(vh160)
    addr = vh160 + h[0:4]
    return base_encode(addr, base=58)

def public_key_to_bc_address(public_key):
    h160 = hash_160(public_key)
    return hash_160_to_bc_address(h160)



def main():
    pass


if __name__ == '__main__':
    main()