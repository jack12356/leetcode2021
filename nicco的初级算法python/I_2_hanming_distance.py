def hanming_distance(m, n) -> int:
    cnt = 0
    while m > 0 and n > 0:
        cnt = cnt + 1 if (m & 1) != (n & 1) else cnt
        m >> 1
        n >> 1
    return cnt
