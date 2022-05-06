def reverse_2_bit(n):
    res = 0
    while n > 0:
        k = n & 1
        n >>= 1
        res <<= 1
        res += k
    return res
