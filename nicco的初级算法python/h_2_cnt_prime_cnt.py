class Solution(object):
    def cnt_prime(self, n):
        if n <= 0:
            return 0
        if n <= 3:
            return n - 1
        dp: [] = [0 for _ in range(n + 1)]
        cnt: int = 0
        for i in range(2, n + 1):
            if dp[i]:
                continue
            cnt += 1
            for j in range(1, n // i + 1):
                dp[j * i] = 1
        return cnt


if __name__ == '__main__':
    for i in range(20):
        print(i, Solution().cnt_prime(i))
