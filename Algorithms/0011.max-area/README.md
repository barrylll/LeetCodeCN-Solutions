# 11. 盛最多水的容器

## 题意

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

**示例1**:

输入: [1,8,6,2,5,4,8,3,7]

输出: 49

## 题解

直接暴力的想法就是双重循环，在最外层循环遍历到每个元素的时候都往前再遍历一次，每次都计算当前的面积，记录最高值。但是这种方法的时间复杂度为`O(n^2)`会超时。

减少时间复杂度的方法就是双指针，一个指向最左，一个指向最右。每次计算两个指针内的区域面积并记录最高值，然后将两个指针指向的值较小的那个指针向较大的移动。这种方法的时间复杂度为`O(n)`

## 标程

```python
from typing import List

class Solution(object):
    def maxArea(self, height: List[int]) -> int:
        ret = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[right], height[left])
            ret = max(ret, area)
            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1
        return ret

if __name__ == '__main__':
    print(
        Solution().maxArea([2, 2])
    )
```