# 75. 颜色分类

## 题意

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

**注意:**

不能使用代码库中的排序函数来解决这道题。

**示例:**
```
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
```

**进阶:**

1.  一个直观的解决方案是使用计数排序的两趟扫描算法。首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
2.	你能想出一个仅使用常数空间的一趟扫描算法吗？

## 题解

设置三个指针，分别为`0`的右边界，`2`的左边界和当前值，分别记为`left`，`right`和`cur`。遍历一遍数组，如果是`0`则与`left`的值互换，`cur`和`left`同时右移，如果是`1`则`cur`右移，如果是`2`则与`right`的值互换，并将`right`左移。

## 标程

```python
from typing import List


class Solution(object):
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = left = 0
        right = len(nums) - 1
        while cur <= right:
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            elif nums[cur] == 1:
                cur += 1
        print(nums)


if __name__ == '__main__':
    print(
        Solution().sortColors([2, 0, 1])
    )

```