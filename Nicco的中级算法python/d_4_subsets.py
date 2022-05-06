from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.subsets_helper(nums, [], 0, res)
        return res

    def subsets_helper(self, nums, cur_lst, idx, res):
        if idx == len(nums):
            res.append([i for i in cur_lst])
            return
        cur_lst.append(nums[idx])
        self.subsets_helper(nums, cur_lst, idx + 1, res)
        cur_lst.remove(nums[idx])
        self.subsets_helper(nums, cur_lst, idx + 1, res)


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))