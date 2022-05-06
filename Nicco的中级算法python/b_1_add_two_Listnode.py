from Nicco的中级算法python import ListNode


class Solution:
    def add_listnode(self, l1: ListNode, l2: ListNode) -> ListNode:
        st: ListNode = ListNode(-1)
        p = st
        over = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            temp = (v1 + v2 + over) % 10
            over = (v1 + v2 + over) // 10
            p.next = ListNode(temp)
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if over == 1:
            p.next = ListNode(1)
        return st.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    print(Solution().add_listnode(l1, l2))
