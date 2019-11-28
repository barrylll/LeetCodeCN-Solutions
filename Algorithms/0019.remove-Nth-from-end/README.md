# 18. 删除链表的倒数第N个节点

## 题意

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

**说明：**

给定的 n 保证是有效的。

**进阶：**

你能尝试使用一趟扫描实现吗？

**示例**:

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

## 题解

设置两个指针，一个指向链表的第1个节点，一个指向链表的第n + 1个节点，将这两个指针同时向链表的尾部移动，那么当第二个指针为空时，第一个指针就指向了倒数第n + 1个节点，此时将第一个指针指向下下个节点即跳过了第n个节点。

## 标程

```python
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
```