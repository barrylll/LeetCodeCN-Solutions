# 74. 搜索二维矩阵

## 题意

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

1.  每行中的整数从左到右按升序排列。
2.  每行的第一个整数大于前一行的最后一个整数。

**示例1:**
```
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
```

**示例2:**
```
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
```

## 题解

二分。开始想的方法是对二元组进行二分，但是需要考虑的问题太多了，所以对`index`进行二分，那么每个数的行坐标为`index // n`，列坐标为`index % n`。

## 标程

```python
from typing import List


class Solution(object):
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right + 1) // 2
            index_row = mid // n
            index_col = mid % n
            if matrix[index_row][index_col] == target:
                return True
            elif matrix[index_row][index_col] > target:
                right = mid - 1
            elif matrix[index_row][index_col] < target:
                left = mid + 1
        return False


if __name__ == '__main__':
    print(
        Solution().searchMatrix([
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 13)
    )

```