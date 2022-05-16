class Solution(object):

    def searchRange(self, nums: [int], target: int) -> []:
        fst: int = self.search_first(nums, target)
        lst: int = self.search_end(nums, target)
        return [fst, lst]

    def search_first(self, nums, target) -> int:
        st = 0
        end = len(nums) - 1
        while st < end:
            mid = st + (end - st) // 2
            if nums[mid] < target:
                st = mid + 1
            else:
                end = mid
        return st if 0 <= st < len(nums) and nums[st] == target else -1

    def search_end(self, nums, target) -> int:
        st = 0
        end = len(nums) - 1
        while st < end:
            mid = st + (end - st + 1) // 2      # 注意这里使用上取整
            if nums[mid] <= target:
                st = mid
            else:
                end = mid - 1
        return end if 0 <= end < len(nums) and nums[end] == target else -1


if __name__ == '__main__':
    a = [1, 2, 4,4,4,4, 6, 7]
    print(Solution().searchRange(a, 3))
