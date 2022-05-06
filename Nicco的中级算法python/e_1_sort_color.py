from typing import List, Optional


class Solution:
    def sortColors(self, nums: Optional[List[int]]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        lf: int = -1
        rt: int = len(nums)
        idx = 0
        while idx < rt:
            if nums[idx] == 0:
                lf += 1
                self.swap(nums, idx, lf)
                idx += 1
            elif nums[idx] == 1:
                idx += 1
            elif nums[idx] == 2:
                rt -= 1
                self.swap(nums, idx, rt)

    def swap(self, nums, x, y):
        t = nums[x]
        nums[x] = nums[y]
        nums[y] = t


if __name__ == '__main__':
    a = [1, 0]
    Solution().sortColors(a)
    print(a)