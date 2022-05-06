def pasika_triple(n):
    if not n:
        return []
    res = [[1]]
    pre = [1]
    for i in range(1, n):
        st = 0
        end = len(pre) - 1
        next = [pre[st]]
        while st <= end:
            if st == end:
                next.append(pre[end])
                break
            next.append(pre[st] + pre[st + 1])
            st += 1
        pre = next
        res.append(next)
    return res


if __name__ == '__main__':
    print(pasika_triple(5))
