# 86. 分隔链表

## 题意

给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

**示例:**
```
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
```

## 题解

维护两个链表，一个存小于`x`的，一个存大于等于`x`的，存完之后把第二个链表的尾部指向`None`，把第一个链表的尾部指向第二个链表的头部即可。

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

```