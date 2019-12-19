# 55. 跳跃游戏

## 题意

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

**示例1:**

```
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
```

**示例2:**

```
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
```

## 题解

用`max_range`记录能跳到的最远距离，对数组进行遍历，遍历时更新`max_range`的值，如果在某个位置无法达到最远距离`max_range`则返回`False`

## 标程

```python
from typing import List


class Solution(object):
    def canJump(self, nums: List[int]) -> bool:
        max_range = nums[0]
        for i in range(len(nums)):
            if i > max_range:
                return False
            max_range = max(max_range, i + nums[i])
        return True


if __name__ == '__main__':
    print(
        Solution().canJump([1, 2, 3, 4, 5])
    )

```