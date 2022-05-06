from typing import Optional, List


def letterCombinations(digits: str) -> Optional[List]:
    map_dict: dict = {'1': "", "2": "abc", '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                      '9': 'wxyz'}
    if not digits:
        return None
    s: str = map_dict.get(digits[0], "")
    next_res: [] = letterCombinations(digits[1:])
    res = []
    for i in s:
        tmp_res: List[str] = [str(i+ns) for ns in next_res] if next_res else [i]
        res.extend(tmp_res)
    return res


if __name__ == "__main__":
    print(letterCombinations('234'))
