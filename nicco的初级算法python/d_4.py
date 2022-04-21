from typing import List

from . import TreeNode


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res: [] = []
        if not root:
            return res
        queue: [] = [root]
        while queue:
            layer: list = []
            for _ in range(len(queue)):
                node: TreeNode = queue.pop(0)
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(layer)
        return res
