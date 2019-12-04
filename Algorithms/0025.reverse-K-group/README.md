# 25. K 个一组翻转链表

## 题意

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

**示例**:

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

**说明**:

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

## 题解

每隔K个节点进行一次翻转意味着我们能确定每次需要翻转的链表对应的表头和表位，因此本题可以拆分成两块来思考：

1.给定一个链表的表头和表尾，如何将这个链表翻转

2.如何将多个翻转后的链表拼接成一个链表

分别解决以上两个问题。首先翻转需要维护三个`ListNode`，分别为`cur`，`pre`，`nxt`，分别表示当前节点，该节点的上一个节点以及下一个节点。在每次操作时，将当前节点的`next`指针指向上一个节点，然后把`pre`设置为当前节点，`cur`设置为下一个节点，`nxt`设置为下一个节点的下一个节点即可。（注意以上的顺序都是按照原链表的顺序表示，具体实现可参考标程代码）

然后将多个翻转后的链表拼接成一个链表采用了递归的方法，每次将链表的前K个节点翻转，然后递归操作整个链表，直到剩下的节点数不足K个。

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
    def reverseGroup(self, head: ListNode, end: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur != end:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        start = end = head
        for i in range(k):
            if not end:
                return head
            end = end.next
        first = self.reverseGroup(start, end)
        start.next = self.reverseKGroup(end, k)
        return first


if __name__ == '__main__':
    print(
        Solution().reverseKGroup(
            ListNode(2, ListNode(3, ListNode(3, ListNode(5)))), 4
        )
    )
```
