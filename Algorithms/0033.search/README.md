# 33. 搜索旋转排序数组

## 题意

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

**示例1:**

输入: nums = [4,5,6,7,0,1,2], target = 0

输出: 4

**示例2:**

输入: nums = [4,5,6,7,0,1,2], target = 3

输出: -1

## 题解

看到`logn`果断二分。首先用二分找到旋转的节点`index`，然后根据`target`的大小判断应该在`index`前进行二分查找还是在`index`后进行二分查找。

## 标程

```python
from typing import List


class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            index = -1
        else:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    index = mid
                    break
                elif nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        if index + 1 == 0:
            return self.Bsearch(nums, target)
        if target >= nums[0]:
            return self.Bsearch(nums[:index + 1], target)
        else:
            return index + 1 + self.Bsearch(nums[index + 1:], target) \
                if self.Bsearch(nums[index + 1:], target) != -1 else -1

    def Bsearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    print(
        Solution().search([6, 7, 8, 1, 2, 3, 4, 5], 6)
    )

```