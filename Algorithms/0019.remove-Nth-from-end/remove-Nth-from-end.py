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


class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ret = ListNode(0)
        ret.next = head
        left = ret
        right = ret
        for i in range(n + 1):
            right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return ret.next


if __name__ == '__main__':
    print(
        Solution().removeNthFromEnd(
            ListNode(2, ListNode(4, ListNode(3))), 2
        )
    )