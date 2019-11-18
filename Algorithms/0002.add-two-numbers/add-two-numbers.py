# -*- coding: utf-8 -*-

"""
LeetCode 0002
https://leetcode-cn.com/problems/add-two-numbers/
author: barryliu
date: 2019-11-18
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
