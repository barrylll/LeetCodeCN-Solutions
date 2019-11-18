# 1. 两数之和

## 题意

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

**示例:**

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]

## 题解

维护一个 `dict` ，遍历每个元素 `x` ，在 `dict` 中查找是否存在一个键与 `target - x` 相等的目标元素，如果不存在，以 `x` 为键，下标为值，存入 `dict` 中。

## 标程

```python
from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, x in enumerate(nums):
            if target - x in hashmap:
                return [hashmap[target - x], i]
            else:
                hashmap[x] = i
        return []

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
```
