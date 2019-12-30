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
    def partition(self, head: ListNode, x: int) -> ListNode:
        f1 = ln1 = ListNode(0)
        f2 = ln2 = ListNode(0)
        cur = head
        while cur:
            if cur.val < x:
                ln1.next = cur
                cur = cur.next
                ln1 = ln1.next
            else:
                ln2.next = cur
                cur = cur.next
                ln2 = ln2.next
        ln2.next = None
        ln1.next = f2.next
        return f1.next


if __name__ == '__main__':
    print(
        Solution().partition(
            ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3
        )
    )
