from typing import List, Optional


class NiccoSortClass(object):
    """
    nicco手动实现各大排序算法
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def BubbleSort(nums: List[int]):
        """
        冒泡排序
        """
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    t = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = t
        return

    @staticmethod
    def selectionSort(nums: List[int]):
        """
        选择排序
        :param nums:
        :return:
        """
        for i in range(len(nums)):
            max_idx = 0
            for j in range(len(nums) - i):
                if nums[j] > nums[max_idx]:
                    max_idx = j
            t = nums[max_idx]
            nums[max_idx] = nums[len(nums) - 1 - i]
            nums[len(nums) - 1 - i] = t
        return

    @staticmethod
    def insertionSort(nums: List[int]):
        for i in range(len(nums)):
            idx = i
            pre_idx = idx - 1
            while pre_idx >= 0 and nums[pre_idx] > nums[idx]:
                t = nums[idx]
                nums[idx] = nums[pre_idx]
                nums[pre_idx] = t
                pre_idx -= 1
                idx -= 1
        return

    def mergeSortmergeSort(self, nums: List[int]):
        def merge(lf_nums: List[int], rt_nums: List[int]) -> List[int]:
            merge_nums: List[int] = []
            while lf_nums and rt_nums:
                if lf_nums[0] <= rt_nums[0]:
                    t = lf_nums.pop(0)
                    merge_nums.append(t)
                else:
                    t = rt_nums.pop(0)
                    merge_nums.append(t)
            if lf_nums:
                merge_nums.extend(lf_nums)
            elif rt_nums:
                merge_nums.extend(rt_nums)
            return merge_nums

        if len(nums) <= 1:
            return nums
        mid: int = len(nums) // 2
        res = merge(self.mergeSortmergeSort(nums[:mid]), self.mergeSortmergeSort(nums[mid:]))
        return res

    @staticmethod
    def quick_sort(nums: List[int]):
        """
        两路快排
        :param nums:
        :return:
        """

        def quick_sort_helper(nums: List[int], low: int, high: int):
            st: int = low
            end: int = high
            key = nums[low]
            while end > st:
                # 从后往前比较
                while end > st and nums[end] >= key:  # 如果没有比关键值小的，比较下一个，直到有比关键值小的交换位置，然后又从前往后比较
                    end -= 1
                if nums[end] <= key:
                    t = nums[end]
                    nums[end] = nums[st]
                    nums[st] = t
                while st < end and nums[st] <= key:  # 如果没有比关键值大的，比较下一个，直到有比关键值大的交换位置
                    st += 1
                if nums[st] >= key:
                    t = nums[end]
                    nums[end] = nums[st]
                    nums[st] = t
            # 此时第一次循环比较结束，关键值的位置已经确定了。左边的值都比关键值小，右边的值都比关键值大，但是两边的顺序还有可能是不一样的，进行下面的递归调用
            if st > low:
                quick_sort_helper(nums, low, st - 1)  # 左边序列。第一个索引位置到关键值索引-1
            if end < high:
                quick_sort_helper(nums, end + 1, high)  # 右边序列。从关键值索引+1到最后一个

        # 调用快排
        quick_sort_helper(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    t_nums = [6, 3, 2, 2, 5, 9, 15, 7]
    nicco_test = NiccoSortClass()
    # nicco_test.BubbleSort(t_nums)
    # nicco_test.selectionSort(t_nums)
    # nicco_test.insertionSort(t_nums)
    # print(nicco_test.mergeSortmergeSort(t_nums))
    nicco_test.quick_sort(t_nums)
    print(t_nums)
