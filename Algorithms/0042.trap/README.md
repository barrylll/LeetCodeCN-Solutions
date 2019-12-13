# 42. 接雨水

## 题意

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

![<rainwatertrap>](<https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png>)

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

**示例:**

```
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
```

## 题解

本题的思路就是计算每一列的积水，然后把每一列的积水相加即最终将结果，而每一列能积的水取决于这一列前后比他高的列的最大值。
一个简单的想法是两次遍历，对每一列都往前往后各遍历一次找到最大值，但是这样的方法时间复杂度为`O(n^2)`提交之后会超时。
因此用一个`list`来存这些数，在每次遍历的时候取当前值和上一位值中的最大值，这样一次遍历就能完成，时间复杂度为`O(n)`。

## 标程

```python
from typing import List


class Solution(object):
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ret = 0
        l_line = [0 for _ in range(len(height))]
        r_line = [0 for _ in range(len(height))]
        l_line[0] = height[0]
        r_line[len(height) - 1] = height[len(height) - 1]
        for i in range(1, len(height)):
            l_line[i] = max(l_line[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            r_line[i] = max(r_line[i + 1], height[i])
        for i in range(len(height)):
            ret += min(r_line[i], l_line[i]) - height[i]
        return ret


if __name__ == '__main__':
    print(
        Solution().trap([2,2])
    )

```