from typing import List
import random


class Solution(object):
    def __init__(self, nums: List[int]):
        self.idx_list = None
        self.nums = nums

    def shuffle(self) -> List[int]:
        idx_list = [i for i in range(len(self.nums))]
        shuffle_idx_list = []
        while idx_list:
            rand_idx_idx = random.randint(0, len(idx_list) - 1)
            choice: int = idx_list.pop(rand_idx_idx)
            shuffle_idx_list.append(choice)
        return [self.nums[i] for i in shuffle_idx_list]

    def reset(self) -> List[int]:
        return self.nums


if __name__ == "__main__":
    nums = [[1], 2, [3, 3, 3]]
    a = Solution(nums)
    print(a.nums)
    print(a.shuffle())
    print(a.shuffle())
    print(a.shuffle())
    print(a.reset())

