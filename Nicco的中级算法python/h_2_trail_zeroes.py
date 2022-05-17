def trailingZeroes(n: int):
    count: int = 0
    while n > 1:
        count += (n // 5)
        n //= 5
    return count
