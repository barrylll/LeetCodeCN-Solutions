# 85. 最大矩形

## 题意

给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

**示例:**
```
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
```

## 题解

这题从题目看就跟84题很像...

对于行都算一次从此行开始往上数的柱状图，如果此行当前位置为`0`则该位置的柱状图值为`0`。例如：
["1", "0", "1", "0", "0"]  
["1", "0", "1", "1", "1"]  
["1", "1", "1", "1", "1"]  
["1", "0", "0", "1", "0"]  
第一行的柱状图为[1, 0, 1, 0, 0]  
第二行的柱状图为[2, 0, 2, 1, 1]  
第三行的柱状图为[3, 1, 3, 2, 2]  
第四行的柱状图为[4, 0, 0, 3, 0]  

然后参考[84. 柱状图中最大的矩形](https://github.com/barrylll/LeetCodeCN-Solutions/tree/master/Algorithms/0084.largestRectangleArea)，对于每一个柱状图都算一次最大值，取全局最大值。

## 标程

```python
from typing import List


class Solution(object):
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0
            max_area = max(max_area, self.cal(heights))
        return max_area

    def cal(self, heights: List[int]):
        ret = 0
        stack = [-1]
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                ret = max(ret, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            ret = max(ret, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return ret


if __name__ == '__main__':
    print(
        Solution().maximalRectangle(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]
            ]
        )
    )

```