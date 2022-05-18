# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = -10**7

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSinglePath(root)
        return self.max_sum

    def maxSinglePath(self,root: TreeNode) -> int:
        if not root:
            return 0
        lf_len = self.maxSinglePath(root.left) if self.maxSinglePath(root.left) > 0 else 0
        rt_len = self.maxSinglePath(root.right) if self.maxSinglePath(root.right) > 0 else 0
        self.max_sum = max(self.max_sum, root.val + lf_len + rt_len)
        return max(lf_len,rt_len) + root.val
