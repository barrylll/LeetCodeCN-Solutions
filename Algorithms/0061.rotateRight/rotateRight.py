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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        temp = head
        n = 0
        cnt = 0
        while temp is not None:
            n += 1
            if temp.next is None:
                end = temp
            temp = temp.next
        if n == 0:
            return head
        k = k % n
        temp = head
        if k == 0:
            return head
        else:
            while temp is not None:
                cnt += 1
                if cnt == n - k:
                    first = temp.next
                    temp.next = None
                    end.next = head
                temp = temp.next
            return first


if __name__ == '__main__':
    print(
        Solution().rotateRight(
            ListNode(2, ListNode(4, ListNode(3))), 1
        )
    )
