# 23. 合并K个排序链表

## 题意

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

**示例**:
```
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
```
## 题解

很容易能想到一种暴力的解法。把链表里的所有值都读出来存到一个`list`中，将这个`list`排序，然后把排序后的`list`构建一个新的链表。读取链表的所有值的时间复杂度为`O(n)`，排序的时间复杂度为`O(n*logn)`，构建新链表的时间复杂度为`O(n)`，总体时间复杂度为`O(n*logn)`。

第二种方法是分治的方法。将输入的`K`个链表按题目要求两两合并，将合并后的结果再两两合并，直到最后只剩下一个链表，这个链表就是题目要求的输出。每次合并的时间复杂度为`O(n)`，合并操作会执行`logk`次，所以最终的时间复杂度为`O(n*logk)`。

## 标程（暴力）

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


class Solution(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ret = ListNode(0)
        l = []
        for list_i in lists:
            while list_i:
                l.append(list_i.val)
                list_i = list_i.next
        l.sort()
        temp = ret
        for val_i in l:
            temp.next = ListNode(val_i)
            temp = temp.next
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
```

## 标程（分治）
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
        Solution().mergeKLists(
        [
            ListNode(2, ListNode(3, ListNode(5))),
            ListNode(1, ListNode(4, ListNode(6))),
            ListNode(7, ListNode(9, ListNode(9)))
        ]
        )
    )
```