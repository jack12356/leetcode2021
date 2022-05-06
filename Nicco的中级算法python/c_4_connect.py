from Nicco的中级算法python import Node


def connect(root: Node):
    if not root:
        return
    queue: list = [root]
    while queue:
        q_lst = []
        for i in range(len(queue)):
            p: Node = queue.pop(0)
            q_lst.append(p)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        for i in range(len(q_lst)):
            p: Node = q_lst[i]
            q: Node = q_lst[i+1] if i+1 < len(q_lst) else None
            p.next = q
    return

