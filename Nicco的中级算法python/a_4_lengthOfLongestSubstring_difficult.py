def lengthOfLongestSubstring_difficult(s:str) -> int:
    p = 0
    lf = -1
    max_len = 0
    map = {}
    while p< len(s):
        char = s[p]
        if map.get(char, -1) != -1:
            last_p = map.get(char)
            lf = last_p
            for key in map.keys():
                map[key] = -1 if map.get(key) < last_p else map.get(key)
        map[char] = p
        max_len = max(max_len, p-lf)
        p+=1
    return max_len


if __name__ == '__main__':
    a = "abcacbcacda"
    print(lengthOfLongestSubstring_difficult(a))

