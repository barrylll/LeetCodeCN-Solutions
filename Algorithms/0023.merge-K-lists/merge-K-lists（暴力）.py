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


class Solution(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ret = ListNode(0)
        l = []
        for list_i in lists:
            while list_i:
                l.append(list_i.val)
                list_i = list_i.next
        l.sort()
        temp = ret
        for val_i in l:
            temp.next = ListNode(val_i)
            temp = temp.next
        return ret.next


if __name__ == '__main__':
    print(
        Solution().mergeKLists([
            ListNode(2, ListNode(3, ListNode(5))),
            ListNode(1, ListNode(4, ListNode(6))),
            ListNode(7, ListNode(9, ListNode(9)))
        ])
    )
