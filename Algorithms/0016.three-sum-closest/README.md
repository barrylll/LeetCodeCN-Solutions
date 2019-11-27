# 16. 最接近的三数之和

## 题意

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

```
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
```
## 题解

跟15题几乎一模一样，题解参考[第15题](https://github.com/hexsix/LeetCodeCN-Solutions/tree/master/Algorithms/0015.three-sum)

## 标程

```python
from typing import List

class Solution(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mi = float("inf")
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = abs(nums[i] + nums[left] + nums[right] - target)
                if temp < mi:
                    ret = nums[i] + nums[left] + nums[right]
                    mi = temp
                if nums[i] + nums[left] + nums[right] - target >= 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] - target < 0:
                    left += 1
        return ret

if __name__ == '__main__':
    print(
        Solution().threeSumClosest([-1, 2, 1, -4], 1)
    )
```