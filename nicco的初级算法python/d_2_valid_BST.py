
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, min_val, max_val):
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)

    # # 二叉树中序遍历
    # def isValidBST_1(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #     nums: list = []
    #     self.inorder(root, nums)
    #     pre: int = int('-inf')
    #     for i in nums:
    #         if pre >= i:
    #             return False
    #         pre = i
    #     return True
    #
    # def inorder(self, root: TreeNode, nums: list) -> None:
    #     if not root:
    #         return
    #     self.inorder(root.left, nums)
    #     nums.append(root.val)
    #     self.inorder(root.right, nums)

    #     前序遍历
    def pre_order(self, root: TreeNode) -> None:
        if not root:
            return
        stack: list = [root]
        while stack:
            node: TreeNode = stack.pop()
            print(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # 中序遍历
    def in_order(self, root: TreeNode) -> None:
        if not root:
            return
        stack: list = []
        node: TreeNode = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.val)
                node = node.right

    # 后序遍历
    def post_order(self, root: TreeNode) -> None:
        if not root:
            return
        stack: list = [root]
        while stack:
            node: TreeNode = stack.pop()
            print(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    # 层序遍历
    def level_order(self, root: TreeNode) -> None:
        if not root:
            return
        queue: list = [root]
        while queue:
            node: TreeNode = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
