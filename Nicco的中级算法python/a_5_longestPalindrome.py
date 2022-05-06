def longestPalindrome(s: str) -> str:
    if not s:
        return s
    dp: [[bool]] = [[False for _ in range(len(s))] for _ in range(len(s))]
    max_len = 0
    res = ""
    for i in range(len(s)):
        for j in range(0, i + 1):
            if s[i] == s[j] and (i - j <= 2 or dp[i - 1][j + 1]):
                dp[i][j] = True
                if i - j + 1 >= max_len:
                    max_len = max(max_len, i - j + 1)
                    res = s[j:i + 1]
    return res


if __name__ == "__main__":
    print(longestPalindrome("babgdad"))