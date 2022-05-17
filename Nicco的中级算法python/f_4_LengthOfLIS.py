"""
求最长子序列
"""


def f_4_LengthOfLIS(nums:[int]) -> int:
    dp: [int] = [1 for _ in nums]
    for i,v in enumerate(nums):
        for j in range(i,-1,-1):
            if nums[i]>nums[j]:
                dp[i] = max(dp[j]+1, dp[i])
    return max(dp)


if __name__=="__main__":
    print(f_4_LengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))