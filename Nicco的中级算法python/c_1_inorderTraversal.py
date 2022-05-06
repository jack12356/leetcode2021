from Nicco的中级算法python import TreeNode

from typing import List


def inorderTraversal(root: TreeNode) -> List[int]:
    res = []
    if not root:
        return res
    res.extend(inorderTraversal(root.left))
    res.append(root.val)
    res.extend(inorderTraversal(root.right))
    return res


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    print(root.inorder())
