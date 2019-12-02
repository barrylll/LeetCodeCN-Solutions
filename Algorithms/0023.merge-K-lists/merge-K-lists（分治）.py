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
        le = len(lists)
        interval = 1
        while interval < le:
            for i in range(0, le - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if le > 0 else None

    def merge2Lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        ret = ListNode(0)
        temp = ret
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if not list1:
            temp.next = list2
        else:
            temp.next = list1
        return ret.next


if __name__ == '__main__':
    print(
        Solution().mergeKLists([
            ListNode(2, ListNode(3, ListNode(5))),
            ListNode(1, ListNode(4, ListNode(6))),
            ListNode(7, ListNode(9, ListNode(9)))
        ]
        )
    )
