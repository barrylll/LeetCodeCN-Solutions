# -*- coding: utf-8 -*-

"""
LeetCode 0002
https://leetcode-cn.com/problems/add-two-numbers/
author: hexsix
date: 2019-09-28
"""

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
        ret = cur = ListNode(0)
        carry = 0
        while l1 or l2:
            val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.next = ListNode(val % 10)
            carry = val // 10
            cur = cur.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            cur.next = ListNode(1)
        return ret.next

if __name__ == '__main__':
    print(Solution().addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3))),
        ListNode(5, ListNode(6, ListNode(4)))
        )
    )
