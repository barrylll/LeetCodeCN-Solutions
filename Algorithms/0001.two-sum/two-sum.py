# -*- coding: utf-8 -*-

"""
LeetCode 0001
https://leetcode-cn.com/problems/two-sum/
author: hexsix
date: 2019-09-27
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, x in enumerate(nums):
            if target - x in hashmap:
                return [hashmap[target - x], i]
            else:
                hashmap[x] = i
        return []

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
