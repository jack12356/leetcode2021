from Nicco的中级算法python import TreeNode


def inorder(root: TreeNode) -> [int]:
    res: [int] = []
    if not root:
        return res
    res.extend(root.left)
    res.append(root.val)
    res.extend(root.right)
    return res


def c_5_KthSmallest(root: TreeNode, k: int) -> int:
    if not root or k <= 0:
        return -1
    res = inorder(root)
    return res[k] if k < len(res) else -1





