# 82. 删除链表中的重复元素 II

## 题意

给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

**示例1:**
```
输入: 1->2->3->3->4->4->5
输出: 1->2->5
```

**示例2:**
```
输入: 1->1->1->2->3
输出: 2->3
```

## 题解

从头到尾扫，遇到连续的相同的元素就全删掉，直接指向这些元素后面那个元素即可。

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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        first = cur = ListNode(0)
        cur.next = head
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                temp = cur.next
                while temp.next and temp.val == temp.next.val:
                    temp = temp.next
                cur.next = temp.next
            else:
                cur = cur.next
        return first.next


if __name__ == '__main__':
    print(
        Solution().deleteDuplicates(
            ListNode(1, ListNode(1))
        )
    )

```