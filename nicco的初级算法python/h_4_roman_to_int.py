def romanToInt(s):
    letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0;
    for i in range(len(s)):
        char = s[i]
        result += dic[char]
        if (i != len(s) - 1):
            if (dic[char] < dic[s[i + 1]]):
                result -= 2 * dic[char]
    return result


tests = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
for i in tests:
    print(i, " ==> ", romanToInt(i))
