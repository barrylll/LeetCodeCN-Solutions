# 73. 矩阵置零

## 题意

给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

**示例1:**
```
输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

**示例2:**
```
输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
```

**进阶：**

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。

一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。

你能想出一个常数空间的解决方案吗？

## 题解

因为要用到常数空间，所以考虑直接在原数组上做标记。先扫一遍，将所有`matrix[i][j] == 0`的对应行和对应列的第一位标记为`0`。
然后再扫一遍，将每一个行和列的初始位置为`0`的数都置为`0`。需要注意的是第一行第一列对应的都是`matrix[0][0]`，所以需要给第一行和第一列都单独标记。

## 标程

```python
from typing import List


class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row = 1
        first_column = 1

        for i in range(m):
            if matrix[i][0] == 0:
                first_column = 0

        for j in range(n):
            if matrix[0][j] == 0:
                first_row = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_column == 0:
            for i in range(m):
                matrix[i][0] = 0
        if first_row == 0:
            for j in range(n):
                matrix[0][j] = 0
        print(matrix)


if __name__ == '__main__':
    print(
        Solution().setZeroes([
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ])
    )

```