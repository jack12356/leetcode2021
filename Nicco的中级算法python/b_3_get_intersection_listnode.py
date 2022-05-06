from typing import Optional

from Nicco的中级算法python import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        st1 = ListNode(-1)
        st1.next = headA
        st2 = ListNode(-1)
        st2.next = headB
        p = st1
        q = st2
        m = 0
        n = 0
        while p.next:
            p = p.next
            m += 1
        while q.next:
            q = q.next
            n += 1
        cnt = m - n if m > n else n - m
        p = st1
        q = st2
        while cnt:
            if m > n:
                p = p.next
            else:
                q = q.next
            cnt -= 1
        while p != q and p and q:
            p = p.next
            q = q.next
        return p if p == q and p else None

if __name__ == '__main__':
    l = ListNode(6)
    l.next = ListNode(7)
    l.next.next = ListNode(8)

    l1 = ListNode(5)
    l1.next = ListNode(3)
    l1.next.next = l

    l2 = ListNode(2)
    l2.next = ListNode(1)
    l2.next.next = ListNode(0)
    l2.next.next.next = l

    print(Solution().getIntersectionNode(l1, l2))