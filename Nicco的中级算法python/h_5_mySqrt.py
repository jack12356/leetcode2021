def mySqrt(x: int):
    if x < 0:
        return None
    if x == 0:
        return 0
    st = 1
    end = x
    while st < end:
        mid = st + (end - st) // 2
        if x // mid == mid:
            return mid
        if x // mid > mid:
            st = mid + 1
        else:
            end = mid
    return st if x // st == st else st - 1


# for i in range(20):
    # print(i)
    # print(mySqrt(i))
mySqrt(9)