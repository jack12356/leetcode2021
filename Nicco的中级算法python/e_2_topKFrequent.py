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

    # def topKFrequent_qk(self, nums: List[int], k: int) -> List[int]:
    #     if k < 0 or k > len(nums):
    #         return []
    #     self.quick_sort_topK(nums, k, 0, len(nums) - 1)
    #     return nums[-k:]
    #
    # def quick_sort_topK(self, nums: List[int], k: int, low: int, high: int):
    #     st = low
    #     end = high
    #     key: int = nums[low]
    #     while st < end:
    #         while st < end and nums[end] >= key:
    #             end -= 1
    #         if st < end:
    #             t = nums[end]
    #             nums[end] = nums[st]
    #             nums[st] = t
    #         while st < end and nums[st] <= key:
    #             st += 1
    #         if st < end:
    #             t = nums[end]
    #             nums[end] = nums[st]
    #             nums[st] = t
    #     if st == len(nums) - k:
    #         return
    #     if st > low:
    #         self.quick_sort_topK(nums, k, low, st - 1)
    #     if st < high:
    #         self.quick_sort_topK(nums, k, st + 1, high)
    #     return


if __name__ == '__main__':
    a = [1, 7, 5, 1, 2, 2, 3]
    print(Solution().topKFrequent(a, 2))
    # print(Solution().topKFrequent_qk(a, 2))
