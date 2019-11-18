# -*- coding: utf-8 -*-

"""
LeetCode 0003
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
author: barryliu
date: 2019-11-18
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = []
        ret = 0
        for i in s:
            L.append(i)
            while len(L) != len(set(L)):
                L = L[1:]
            ret = max(ret, len(L))
        return ret

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
    print(Solution().lengthOfLongestSubstring('bbbb'))
    print(Solution().lengthOfLongestSubstring('pwwkew'))