# 34. 在排序数组中查找元素的第一个和最后一个位置

## 题意

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

**示例1:**

输入: nums = [5,7,7,8,8,10], target = 8

输出: [3,4]

**示例2:**

输入: nums = [5,7,7,8,8,10], target = 6

输出: [-1,-1]

## 题解

看到`logn`果断二分。分两次二分，在`mid`值等于`target`值时一次往左找，一次往右找，找到目标区间的上界和下界即可。

## 标程

```python
from typing import List


class Solution(object):
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        ma = left = 0
        mi = right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                mi = min(mi, mid)
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ma = max(ma, mid)
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if ma == 0 and mi == len(nums) - 1:
            ma = mi = -1
        ret = [mi, ma]
        return ret


if __name__ == '__main__':
    print(
        Solution().searchRange([1], 1)
    )
```