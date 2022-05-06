from Nicco的中级算法python import TreeNode

from typing import Optional,List


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
        return None
    rt_val = preorder[0]
    rt_idx = inorder.index(rt_val)
    lf_len: int = rt_idx
    rt_len: int = len(inorder) - rt_idx - 1
    root: TreeNode = TreeNode(rt_val)
    root.left = buildTree(preorder[1: lf_len + 1], inorder[:rt_idx])
    root.right = buildTree(preorder[lf_len + 1:], inorder[rt_idx+1:])
    return root


if __name__ == '__main__':
    buildTree([3,9,20,15,7],[9,3,15,20,7])