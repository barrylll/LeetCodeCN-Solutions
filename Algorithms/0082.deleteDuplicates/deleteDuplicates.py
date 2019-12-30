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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        first = cur = ListNode(0)
        cur.next = head
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                temp = cur.next
                while temp.next and temp.val == temp.next.val:
                    temp = temp.next
                cur.next = temp.next
            else:
                cur = cur.next
        return first.next


if __name__ == '__main__':
    print(
        Solution().deleteDuplicates(
            ListNode(1, ListNode(1))
        )
    )
