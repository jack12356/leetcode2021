from typing import List


class BinarySearch(object):
    def bi_search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        st = 0
        end = len(nums) - 1
        while st < end:
            mid = st + (end - st) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid
            else:
                st = mid + 1
        if st < len(nums) and nums[st] == target:
            return st
        return -1

    def find_first(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        st = 0
        end = len(nums) - 1
        while st < end:
            mid = st + (end - st) // 2
            if nums[mid] >= target:
                end = mid
            else:
                st = mid + 1
        return st if nums[st] == target else -1

    def find_last(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        st = 0
        end = len(nums) - 1
        while st < end:
            mid = st + (end - st + 1) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                st = mid
        return end if nums[end] == target else -1


if __name__ == '__main__':
    a = [1, 2, 5, 5, 7, 9, 10]
    # print(BinarySearch().bi_search(a, 1))
    print(BinarySearch().find_first(a, 5))
    print(BinarySearch().find_last(a, 5))
