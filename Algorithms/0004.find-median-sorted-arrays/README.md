# 4. 寻找两个有序数组的中位数

## 题意

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

**示例1**:

nums1 = [1, 3]

nums2 = [2]

则中位数是 2.0

**示例2**:

nums1 = [1, 2]

nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

## 题解

中位数即保证在中位数左边的数的个数等于右边，且左边的最大值小于右边的最小值。

假设两个数组分别为`nums1`和`nums2`，在第一个数组中的分隔位置为`i`，在第二个数组中的分隔位置为`j`，则由上述中位数定义应有
```
i + j = len(nums1) - i + len(nums2) - j
```
即由`i`可推算出
```
j = (len(nums1) + len(nums2) + 1)//2 - i
```
即寻找一个合适的`i`值保证
```
max(nums1[i-1],num2[j-1]) <= min(nums1[i],nums2[j])
```
又因为
```
nums1[i-1] < num1[i], nums2[j-1] < nums2[j]
```
则只需保证
```
nums2[j-1] <= nums1[i]
```
即可。

因为题目要求时间复杂度为`O(log(m + n))`，因此采用二分的方法进行计算`i`。

## 标程

```python
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
```

## 题解 2

[寻找两个有序数组的中位数 C / C++](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/4-xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-shu/)

## 标程 2

```python
from typing import List

class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        
        lo, hi = 0, 2 * n
        while lo <= hi:
            c1 = (lo + hi) // 2
            c2 = m + n - c1

            LMax1 = float('-inf') if c1 == 0 else nums1[(c1 - 1) // 2]
            RMin1 = float('inf') if c1 == 2 * n else nums1[c1 // 2]
            LMax2 = float('-inf') if c2 == 0 else nums2[(c2 - 1) // 2]
            RMin2 = float('inf') if c2 == 2 * m else nums2[c2 // 2]

            if LMax1 > RMin2:
                hi = c1 - 1
            elif LMax2 > RMin1:
                lo = c1 + 1
            else:
                break
        return (max(LMax1, LMax2) + min(RMin1, RMin2)) / 2.0
```