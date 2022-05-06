from typing import List


def groupAnagrams(lst: List[str]) -> []:
    res: List[List[str]] = []
    while lst:
        now = lst.pop()
        nt = {}
        for i in now:
            nt[i] = nt.get(i, 0)+1
        find_flag: bool = False
        for r in res:
            rt = {}
            for i in r[0]:
                rt[i] = rt.get(i, 0) + 1
            if nt == rt:
                r.append(now)
                find_flag = True
                break
        if not find_flag:
            res.append([now])
    return res


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))