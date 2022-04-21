from typing import Optional
from . import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue: [TreeNode] = [root]
        while queue:
            res: [int] = []
            for i in range(len(queue)):
                node: TreeNode = queue.pop(0)
                if node:
                    res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append(None)
            if not self.is_symmetric(res):
                return False
        return True

    def is_symmetric(self, res: [int]):
        if not res or len(res) == 1:
            return True
        if len(res) % 2 != 0:
            return False
        lf = 0
        rt = len(res) - 1
        while lf < rt:
            if res[lf] != res[rt]:
                return False
            lf += 1
            rt -= 1
        return True
