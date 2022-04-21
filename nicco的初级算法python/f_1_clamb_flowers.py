class Solution:
    def find(self, n):
        if n <= 0:
            return -1
        if 0 <= n <= 3:
            return n
        return self.find(n - 1) + self.find(n - 2)

    def climbStairs(self, n: int):
        if n <= 3:
            return n
        dp: [int] = [-1 for _ in range(n+1)]
        for i in range(4):
            dp[i] = i
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]



print(Solution().find(4))
