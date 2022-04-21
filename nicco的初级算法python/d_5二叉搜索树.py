from . import TreeNode
from typing import Optional


class Solution:
    def sortedArrayToBST(self, nums: []) -> Optional[TreeNode]:
        if not nums:
            return None
        mid: int = int(len(nums)/2)
        root: TreeNode = TreeNode(nums[mid])
        left_node = self.sortedArrayToBST(nums[:mid])
        rt_node = self.sortedArrayToBST(nums[mid+1:])
        root.left = left_node
        root.right = rt_node
        return root
