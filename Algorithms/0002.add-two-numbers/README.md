# 2. 两数相加

## 题意

给出两个 **非空** 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 **逆序** 的方式存储的，并且它们的每个节点只能存储 **一位** 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例:**

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)

输出：7 -> 0 -> 8

原因：342 + 465 = 807

## 题解

模拟多位数加法运算的规则，将两个多位数从个位数开始逐个相加，对于题目中的链表来说就是将两个链表从表头开始逐个相加，如果两数相加大于10则进一位，在下一位两数相加时额外加1.

## 标程

```python
# Definition for singly-linked list. (extend __str__() for print())
class ListNode(object):
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = temp = ListNode(0)
        val = 0
        while l1 or l2 or val:
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            temp.next = ListNode(val % 10)
            val //= 10
            temp = temp.next
        return ret.next

if __name__ == '__main__':
    print(Solution().addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3))),
        ListNode(5, ListNode(6, ListNode(4)))))
```