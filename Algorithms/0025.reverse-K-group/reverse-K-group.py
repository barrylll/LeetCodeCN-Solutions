from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        ret = []
        cur = self
        while cur is not None:
            ret.append(cur.val)
            cur = cur.next
        return str(ret)


class Solution:
    def reverseGroup(self, head: ListNode, end: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur != end:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        start = end = head
        for i in range(k):
            if not end:
                return head
            end = end.next
        first = self.reverseGroup(start, end)
        start.next = self.reverseKGroup(end, k)
        return first


if __name__ == '__main__':
    print(
        Solution().reverseKGroup(
            ListNode(2, ListNode(3, ListNode(3, ListNode(5)))), 4
        )
    )
