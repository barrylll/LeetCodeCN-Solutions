# 23. 合并K个排序链表

## 题意

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

**你不能只是单纯的改变节点内部的值**，而是需要实际的进行节点交换。

**示例**:

给定 1->2->3->4, 你应该返回 2->1->4->3.

## 题解

对链表中的每两个结点进行交换，就是把每个结点的`next`指针指向对方本来指向的目标，需要注意这两个结点的前一个结点的指针也需要更改。

## 标程

```python
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
```
