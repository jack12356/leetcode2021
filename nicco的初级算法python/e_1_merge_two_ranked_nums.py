# 合并两个有序数组
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6], n = 3
# 输出: [1,2,2,3,5,6]
class Solution:
    def xxx(self, nums1: [], nums2: [], m, n) -> None:
        if not nums2:
            return
        for i in range(m - 1, -1, -1):
            nums1[i + n] = nums1[i]
            nums1[i] = 0
        lf = 0
        rt = n
        while nums2 and rt < m + n:
            n1 = nums1[rt]
            n2 = nums2[0]
            if n1 <= n2:
                nums1[lf] = nums1[rt]
                nums1[rt] = 0
                lf += 1
                rt += 1
            else:
                nums2.pop(0)
                nums1[lf] = n2
                lf += 1
        if nums2:
            for i in nums2:
                nums1[lf] = i
                lf += 1


a = [1, 2, 3, 0, 0]
b = [2, 5]
Solution().xxx(a, b, 3, 2)
print(a)
