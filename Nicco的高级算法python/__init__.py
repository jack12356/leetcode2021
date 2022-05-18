from typing import List


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


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


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __repr__(self):
        s = ""
        p = self
        while p:
            s = s + " -> " + str(p.val)
            p = p.next
        return s[4:]


test_root = TreeNode(0)
test_root.left = TreeNode(1)
test_root.right = TreeNode(2)

st = ListNode(-1)
p = st
for i in range(5):
    p.next = ListNode(i)
    p = p.next
# print(st.__str__())
