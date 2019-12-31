# 92. 反转链表 II

## 题意

反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

**说明:**

1 ≤ m ≤ n ≤ 链表长度。

**示例:**
```
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
```
## 题解

遍历一遍链表，维护另一个链表倒序存储从`m`到`n`的节点，然后把前边和后边都接上即可。本题主要还是考验对链表操作的熟悉程度。

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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        cnt = 0
        m_node = ListNode(0)
        n_node = ListNode(0)
        first = cur = ListNode(0)
        cur.next = head
        rev = ListNode(0)
        while cur:
            if m < cnt < n:
                nxt = cur.next
                cur.next = rev.next
                rev.next = cur
                cur = nxt
            if cnt == m:
                n_node = rev.next = cur
                cur = cur.next
                rev.next.next = None
            if cnt == m - 1:
                m_node = cur
                cur = cur.next
            if cnt == n:
                nxt = cur.next
                cur.next = rev.next
                rev.next = cur
                cur = nxt
                n_node.next = cur
                m_node.next = rev.next
                break
            if cnt < m - 1:
                cur = cur.next
            cnt += 1
        return first.next


if __name__ == '__main__':
    print(
        Solution().reverseBetween(
            ListNode(1, ListNode(2)), 1, 1
        )
    )

```