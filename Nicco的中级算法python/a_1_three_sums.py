def three_sums(nums: [int], target: int) -> []:
    if len(nums) < 3:
        return []
    nums = sorted(nums)
    res: list = []
    for idx, n in enumerate(nums):
        t: int = target - n
        lf = idx + 1
        rt = len(nums) - 1
        while lf < rt:
            if nums[lf] + nums[rt] == t:
                res.append([n, nums[lf], nums[rt]])
                lf += 1
                rt -= 1
            elif nums[lf] + nums[rt] > t:
                rt -= 1
            else:
                lf += 1
    return res


if __name__ == '__main__':
    a = [1, 4, 5, 6, 8, 10]
    print(three_sums(a, 15))

