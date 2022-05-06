from typing import Optional
from Nicco的中级算法python import ListNode


def oddEvenList(head: ListNode) -> Optional[ListNode]:
    if not head:
        return None
    second = head.next
    p: ListNode = head
    q: ListNode = head.next
    while q and q.next:
        p.next = q.next
        q.next = q.next.next
        p = p.next
        q = q.next
    p.next = second
    return head


