from typing import List

"""
把自己绕晕了，其实就是dp[i]为当前最佳选项情况下的收益
dp[i] = max(dp[i-2]+nums[i], dp[i-1])   # 偷或者不偷
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return nums[0] if len(nums) == 1 else max(nums[0], nums[1])
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[len(nums) - 1]


Solution().rob([2, 1, 1, 2])
