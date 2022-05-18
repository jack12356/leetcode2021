from Nicco的高级算法python import ListNode


def merge(st1: ListNode, st2: ListNode):
    st = ListNode(-1)
    cur = st
    while st1 and st2:
        if st1.val < st2.val:
            cur.next = st1
            st1 = st1.next
        else:
            cur.next = st2
            st2 = st2.next
        cur = cur.next
    if not st1:
        cur.next = st2
    elif not st2:
        cur.next = st1
    return st.next


def sortListNode(head: ListNode):
    # 找到中间节点
    if not head or not head.next:
        return head
    fst: ListNode = ListNode(-1)
    lst: ListNode = ListNode(-1)
    fst.next = head
    lst.next = head
    while lst and lst.next:
        fst = fst.next
        lst = lst.next.next
    # 排序
    lst = fst.next
    fst.next = None
    st1 = sortListNode(head)
    st2 = sortListNode(lst)
    # 合并后返回
    return merge(st1, st2)


if __name__ == '__main__':
    ls = [1]
    st = ListNode(-1)
    t = st
    for i in ls:
        t.next = ListNode(i)
        t = t.next
    print(sortListNode(st.next))

