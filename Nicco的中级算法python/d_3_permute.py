class Solution(object):
    def permute_help(self, nums: list, cur_lst: [], rest_idxs: [], res: []):
        """
        1、终止条件
        2、遍历所有可能节点选择和往下走
        3、恢复状态
        :param nums: 全局变量
        :param cur_lst: 状态变量，存储当前状态
        :param rest_idxs: 状态变量，代表当前进度
        :param res: 全局变量，存出结果
        :return: 空函数
        """

        if not rest_idxs:
            add = [nums[i] for i in cur_lst]
            res.append(add)
        for idx in rest_idxs:
            cur_lst.append(idx)
            rest_idxs_new = [i for i in rest_idxs if i != idx]
            self.permute_help(nums, cur_lst, rest_idxs_new, res)
            cur_lst.remove(idx)

    def permute(self, nums: [int]) -> []:
        res: [[]] = []
        self.permute_help(nums, [], range(len(nums)), res)
        return res


if __name__ == '__main__':
    a = [1, 2, 3]
    res = Solution().permute(a)
    print(res)
