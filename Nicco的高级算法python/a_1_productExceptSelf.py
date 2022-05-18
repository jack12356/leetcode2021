def productExceptSelf(output: [int]):
    if not output:
        return
    lf: [int] = [1 for _ in output]
    rt: [int] = [1 for _ in output]
    for i in range(len(lf)):
        lf[i] = lf[i - 1] * output[i - 1] if i != 0 else lf[i]
    for i in range(len(lf) - 1, -1, -1):
        rt[i] = rt[i + 1] * output[i + 1] if i != len(rt) - 1 else rt[i]
    for i in range(len(output)):
        output[i] = lf[i] * rt[i]
    return


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    productExceptSelf(a)
    print(a)
