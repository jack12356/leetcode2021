from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lf: int = 0
        rt: int = 0
        while rt < len(nums):
            if nums[lf] == nums[rt]:
                rt += 1
            else:
                tmp: int = nums[rt]
                nums[rt] = nums[lf + 1]
                nums[lf + 1] = tmp
                lf += 1
                rt += 1
        return lf+1
