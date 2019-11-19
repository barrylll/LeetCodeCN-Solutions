# 4. 寻找两个有序数组的中位数

## 题意

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

`示例1`:

nums1 = [1, 3]

nums2 = [2]

则中位数是 2.0

`示例2`:

nums1 = [1, 2]

nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

## 题解

中位数即保证在中位数左边的数的个数等于右边，且左边的最大值小于右边的最小值。

假设两个数组分别为`nums1`和`nums2`，在第一个数组中的分隔位置为`i`，在第二个数组中的分隔位置为`j`，则由上述中位数定义应有`i + j = len(nums1) - i + len(nums2) - j`，即由`i`可推算出`j`为`(len(nums1) + len(nums2) + 1)//2 - i`，那么只要有一个合适的`i`值能够保证`max(nums1[i-1],num2[j-1]) <= min(nums1[i],nums2[j])`即可，又因为`nums1[i-1] < num1[i], nums2[j-1] < nums2[j]`，则只需保证`nums2[j-1] <= nums1[i]`即可。

因为题目要求时间复杂度为`O(log(m + n))`，因此采用二分的方法进行计算`i`。

## 标程

```python
from typing import List
class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        #保证num1的长度小于nums2
        left = 0
        right = m
        while left < right:
            i = (left + right)//2
            j = (m + n + 1)//2 - i
            if nums1[i] < nums2[j - 1]:
                left = i + 1
            else:
                right = i
        i = left
        j = (m + n + 1)//2 - i
        c1 = max(nums1[i - 1] if i > 0 else float("-inf"), nums2[j - 1] if j > 0 else float("-inf"))
        c2 = min(nums1[i] if i < m else float("inf"), nums2[j] if j < n else float("inf"))
        if (m + n) % 2 == 1:
            return c1
        return (c1 + c2) / 2

if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
```