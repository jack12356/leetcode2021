def missing_num(nums: []) -> int:
    l = len(nums)
    return l*(l+1)//2 - sum(nums)


if __name__ == '__main__':
    print(missing_num([1, 4, 2, 3]))
