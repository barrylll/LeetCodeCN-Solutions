# 61. 旋转链表

## 题意

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

**示例1:**

```
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
```

**示例2:**

```
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
```

## 题解

设`n`为链表的长度，那么`k > n`时只需旋转`k % n`次（因为每旋转`n`次都会旋转回最初的顺序），记录链表最尾位的节点为`end`，
从头遍历到第`n - k`位，记录`n - k`的下一位为`first`，将`n - k`的下一位指向`None`，将`end`的下一位指向`head`，此时`first`就是所求的链表。

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

```