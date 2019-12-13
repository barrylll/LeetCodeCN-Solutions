<<<<<<< HEAD
# 45. 跳跃游戏 II
=======
# 44. 通配符匹配
>>>>>>> e48622d313a371377eb2a8400c68736df54fb46c

## 题意

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

**示例:**

```
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
```

**说明:**

假设你总是可以到达数组的最后一个位置。

## 题解

贪心，每次跳的时候跳到"此次跳的距离"+"下次能跳的最大距离"最大的那个位置。

## 标程

```python
from typing import List

class Solution(object):
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cnt = i = 0
        while i < len(nums):
            if i + nums[i] + 1 >= len(nums):
                return cnt + 1
            else:
                ma = 0
                for j in range(i + 1, i + nums[i] + 1):
                    if nums[j] + j - i >= ma:
                        ma = nums[j] + j - i
                        nex = j
                i = nex
                cnt += 1


if __name__ == '__main__':
    print(
        Solution().jump([10,9,8,7,6,5,4,3,2,1,1,0])
    )

```