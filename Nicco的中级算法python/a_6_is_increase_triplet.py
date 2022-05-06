from typing import List


def is_incresing_triplet(nums: List[int]) -> bool:
    if len(nums) <= 2:
        return False
    mid: int = 2 ** 32
    min_n: int = 2 ** 32
    for i, n in enumerate(nums):
        if n <= min_n:
            min_n = n
        else:
            if n <= mid:
                mid = n
            else:
                return True
    return False


def is_incresing_triplet1(nums: List[int]) -> bool:
    if len(nums) <= 2:
        return False
    lower = [0 for _ in nums]
    min_n = 2 ** 32
    for i in range(len(nums)):
        if nums[i] > min_n:
            lower[i] = 1
        else:
            min_n = nums[i]
    max_n = -2 ** 32
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < max_n:
            if lower[i] == 1:
                return True
        else:
            max_n = nums[i]
    return False


if __name__ == '__main__':
    print(is_incresing_triplet([1, 2, 1, 8]))
