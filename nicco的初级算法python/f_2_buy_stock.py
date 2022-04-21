from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_v = prices[-1]
        res = 0
        for i in range(len(prices) - 1, -1, -1):
            res = max(max_v - prices[i], res)
            max_v = max(max_v, prices[i])
        return res
