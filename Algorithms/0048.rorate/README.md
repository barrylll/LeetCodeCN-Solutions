# 48. 旋转图像

## 题意

给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

**说明:**
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

**示例1:**

```
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

**示例2:**

```
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

## 题解

很容易发现规律，`matrix[i][j]`位置的数会去到`matrix[n - j][i]`上，所以每次交换一个四元组：
`matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]`
注意判断一下已经交换过的不能再交换即可。

## 标程

```python
from typing import List


class Solution(object):
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        moved = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not moved[i][j] and not moved[n - j - 1][i] and not moved[n - i - 1][n - j - 1] and not moved[j][n - i - 1]:
                    matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = \
                        matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
                    moved[i][j] = moved[n - j - 1][i] = moved[n - i - 1][n - j - 1] = moved[j][n - i - 1] = True
        print(matrix)


if __name__ == '__main__':
    print(
        Solution().rotate([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
    )

```