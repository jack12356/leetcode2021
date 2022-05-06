from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k < 0 or k > len(nums):
            return []
        map_cnt = {}
        for i in nums:
            map_cnt[i] = map_cnt.get(i, 0) + 1
        lst = [(k, v) for k, v in map_cnt.items()]
        lst = sorted(lst, key=lambda x: x[1])
        return [x[0] for x in lst[-k:]]


if __name__ == '__main__':
    a = [1, 1, 1, 2, 2, 3]
    print(Solution().topKFrequent(a, 2))
