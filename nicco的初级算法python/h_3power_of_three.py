class Solution:
    def power_of_three(self, n: int) -> bool:
        if n < 3:
            return False
        k = 1
        while k < n:
            k = k * 3
        return k == n


if __name__ == '__main__':
    print(Solution().power_of_three(27))
