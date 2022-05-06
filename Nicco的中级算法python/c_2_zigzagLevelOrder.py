from Nicco的中级算法python import TreeNode, test_root


def zigzagLevelOrder(root: TreeNode):
    res = []
    if not root:
        return res
    queue = [root]
    reverse: bool = False
    while queue:
        cnt = len(queue)
        add = []
        for i in range(cnt):
            p = queue.pop(0)
            add.append(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        if reverse:
            add = add[::-1]
        reverse = not reverse
        res.append(add)
    return res


if __name__ == '__main__':
    print(zigzagLevelOrder(test_root))
