from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    def inorder(self):
        return self.inorderTraversal(self)

    def inorderTraversal(self, root) -> List[int]:
        res = []
        if not root:
            return res
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res

    def serialize(self):
        res = []
        self.dfs(self, res)
        return res

    def dfs(self, root, res):
        if not root:
            res.append(None)
            return
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

    @staticmethod
    def deserialize(res: [int]):
        index = [0]
        root = TreeNode.deserialize_help(res, index)
        return root

    @staticmethod
    def deserialize_help(res, index: [int]):
        val = res[index[0]]
        index[0] += 1
        if not val:
            return None
        root = TreeNode(val)
        root.left = TreeNode.deserialize_help(res, index)
        root.right = TreeNode.deserialize_help(res, index)
        return root


if __name__ == '__main__':
    a = [1, 2, None, None, 3, 4, None, None, 5, None, None]
    root = TreeNode.deserialize(a)
    print(root.serialize())
