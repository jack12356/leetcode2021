from typing import List


class Solution:
    #  冒泡排序
    def findKthLargest_boble(self, nums: List[int], k: int) -> int:
        if k <= 0 or k > len(nums):
            return -1
        for i in range(k):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    t = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = t
        return nums[-k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort_k(nums: List[int], low: int, high: int, k: int):
            st = low
            end = high
            key = nums[low]
            while st < end:
                while end > st and nums[end] >= key:
                    end -= 1
                if nums[end] < key:
                    t = nums[st]
                    nums[st] = nums[end]
                    nums[end] = t
                while st < end and nums[st] <= key:
                    st += 1
                if nums[st] > key:
                    t = nums[st]
                    nums[st] = nums[end]
                    nums[end] = t
            if st == len(nums) - k:
                return
            if st > low:
                quick_sort_k(nums, low, st - 1, k)
            if end < high:
                quick_sort_k(nums, end + 1, high, k)

        quick_sort_k(nums, 0, len(nums) - 1, k)
        return nums[-k]


if __name__ == "__main__":
    a = [3, 2, 1, 5, 6, 4]
    print(Solution().findKthLargest(a, 4))
