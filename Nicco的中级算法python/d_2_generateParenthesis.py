from typing import List, Optional


class Solution:
    def generateParenthesis(self, n: int) -> Optional[List[str]]:
        res = []
        self.generateParenthesis_help(n, n, res, "")
        return res

    def generateParenthesis_help(self, lf_num, rt_num, res, s: str):
        # 结束条件
        if lf_num == 0 and rt_num == 0:
            res.append(s)
            return
        # 选择
        if lf_num < 0:
            return
        if lf_num > rt_num:
            return
        self.generateParenthesis_help(lf_num - 1, rt_num, res, s + "(")
        self.generateParenthesis_help(lf_num, rt_num - 1, res, s + ")")


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(2))
