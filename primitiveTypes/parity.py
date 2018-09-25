def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


def parity2(x):
    result = 0
    while x:
        result ^= 1
        x &= x-1
    return result


def parity3(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 42
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1