# -*- coding: utf-8 -*-

from typing import List

class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 num1 的长度小于 nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m
        while left < right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            if nums1[i] < nums2[j - 1]:
                left = i + 1
            else:
                right = i
        i = left
        j = (m + n + 1) // 2 - i
        c1 = max(nums1[i - 1] if i > 0 else float("-inf"), nums2[j - 1] if j > 0 else float("-inf"))
        c2 = min(nums1[i] if i < m else float("inf"), nums2[j] if j < n else float("inf"))
        if (m + n) % 2 == 1:
            return c1
        return (c1 + c2) / 2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))