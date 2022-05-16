def uniquePaths(m: int, n: int) -> int:
    if m <= 0 or n <= 0:
        return 0
    dp: [[int]] = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    print(uniquePaths(3, 2))
