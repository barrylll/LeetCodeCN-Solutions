# 84. 柱状图中最大的矩形

## 题意

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

![<histogram>](<https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram.png>)

    以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

![<histogram_area>](<https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram_area.png>)

    图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

**示例:**
```
输入: [2,1,5,6,2,3]
输出: 10
```

## 题解

自己写了一个`O(n^2)`超时了...题解参考了官方题解，用栈来存储过程中的状态，思路是遍历一遍`heights`，如果遇到`heights[i]`大于栈顶元素就入栈，
否则将栈里的元素出栈直到栈顶元素小于`heights[i]`。在出栈的过程中每一次出栈都能保证从栈顶的位置到`i`中间能够成一个矩形（自己画个图就明白了），
因此对于出栈时的每一个元素计算面积为：`area = heights[stack.pop()] * (i - stack[-1] - 1)`。遍历结束后如果仍有元素在栈内，
则说明该元素到`heights[-1]`中间的元素都大于它，此时对于每个栈内的元素计算面积为：`heights[stack.pop()] * (len(heights) - stack[-1] - 1)`

## 标程

```python
from typing import List


class Solution(object):
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ret = 0
        stack = [-1]
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                ret = max(ret, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            ret = max(ret, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return ret


if __name__ == '__main__':
    print(
        Solution().largestRectangleArea(
            [4, 2, 0, 3, 2, 4, 3, 4]
        )
    )

```