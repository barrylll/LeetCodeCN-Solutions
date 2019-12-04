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
    def swapPairs(self, head: ListNode) -> ListNode:
        first = temp = ListNode(0)
        temp.next = head
        while temp and temp.next and temp.next.next:
            l = temp.next
            r = temp.next.next
            l.next = r.next
            r.next = l
            temp.next = r
            temp = l
        return first.next


if __name__ == '__main__':
    print(
        Solution().swapPairs(
            ListNode(2, ListNode(3, ListNode(5)))
        )
    )
