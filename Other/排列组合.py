class Solution(object):

    def target_combination(self, nums: [int], target: int) -> [[]]:
        res = []
        self.combination_helper(nums, target, [], 0, res)
        return res

    def combination_helper(self, nums, target, cur_idx_lst: [int], idx: int, res: [[]]):
        if idx == len(nums):
            return
        if sum([nums[i] for i in cur_idx_lst]) == target:
            res.append([nums[i] for i in cur_idx_lst])
            return
        cur_idx_lst.append(idx)
        self.combination_helper(nums, target, cur_idx_lst, idx+1, res)
        cur_idx_lst.pop(-1)
        self.combination_helper(nums, target, cur_idx_lst,idx+1, res)

    def combination(self, nums: [int]) -> [[]]:
        """
        数组的组合
        :param nums:
        :return:
        """
        if not nums:
            return [[]]
        res_list: [[]] = []
        others = nums[1:]
        others_cbns: [[]] = self.combination(others)
        for os in others_cbns:
            res_list.append([nums[0]] + os)
            res_list.append(os)
        return res_list

    def combination_2(self, nums: [int], idx: int) -> [[]]:
        """
        数组的组合
        :param idx:
        :param nums:
        :return:
        """
        if idx == len(nums):
            return [[]]
        res_list: [[]] = []
        others_cbns: [[]] = self.combination_2(nums, idx + 1)
        for os in others_cbns:
            res_list.append([nums[idx]] + os)
            res_list.append(os)
        return res_list

    def permute(self, nums: [int]) -> [[]]:
        """
        数组的排列
        :param nums:
        :return:
        """
        if not nums:
            return []
        res_list: [[]] = []
        for i in nums:
            others = [t for t in nums if t != i]
            oth_per_lst: [[]] = self.permute(others)
            if not oth_per_lst:
                res_list.append([i])
            else:
                for o in oth_per_lst:
                    res_list.append([i] + o)
        return res_list


if __name__ == '__main__':
    a = [1, 2, 3,4,5,6]
    # print(Solution().permute(a))
    # print(Solution().combination(a))
    # print(Solution().combination_2(a, 0))
    print(Solution().target_combination(a,12))