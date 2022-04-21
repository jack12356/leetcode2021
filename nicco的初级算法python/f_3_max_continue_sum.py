from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n: int = len(nums)
        dp: [[int]] = [[0 for _ in range(n)] for _ in range(n)]
        m = -2**32
        for i in range(n):
            for j in range(i, n):
                dp[i][j] = nums[j] if i == j else dp[i][j-1]+nums[j]
                m = max(m, dp[i][j])
        return m


    def method_2(self,nums:List[int]):
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(nums[i] + max(dp[i - 1], 0))
        return max(dp)