# 81. 搜索旋转排序数组 II

## 题意

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

**示例1:**
```
输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
```

**示例2:**
```
输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
```

**进阶：**
1.  这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
2.  这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

## 题解

二分。参考[第33题](https://github.com/barrylll/LeetCodeCN-Solutions/tree/master/Algorithms/0033.search)。

## 标程

```python
from typing import List


class Solution(object):
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True if nums[0] == target else False
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]:
                left += 1
                continue
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == '__main__':
    print(
        Solution().search([1, 3, 1, 1, 1], 3)
    )

```