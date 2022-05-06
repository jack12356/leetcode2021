class Solution(object):
    def fuzzbizz(self, n: int) -> [str]:
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("fuzzbizz")
            elif i % 3 == 0:
                res.append("fuzz")
            elif i % 5 == 0:
                res.append("bizz")
            else:
                res.append(str(i))
        return res
