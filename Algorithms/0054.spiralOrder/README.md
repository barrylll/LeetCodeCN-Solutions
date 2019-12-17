# 52. N皇后II

## 题意

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

**示例1:**

```
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
```

**示例2:**

```
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## 题解

维护一个二维数组`check`，表示某个点是否被遍历到过，遍历的过程就是
1.  往右走到头就往下转
2.  往下走到头就往左转
3.  往左走到头就往上转
4.  往上走到头就往右转
5.  某个地方既不能继续往前走，也不能转的时候输出结果

## 标程

```python
from typing import List


class Solution(object):
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        check = [[False for _ in range(n)] for _ in range(m)]

        def go_right(row=0, col=0):
            ret.append(matrix[row][col])
            check[row][col] = True
            if (col == n - 1 or check[row][col + 1]) and (row == m - 1 or check[row + 1][col]):
                return ret
            elif col == n - 1 or check[row][col + 1]:
                go_down(row + 1, col)
            else:
                go_right(row, col + 1)

        def go_left(row, col):
            ret.append(matrix[row][col])
            check[row][col] = True
            if (col == 0 or check[row][col - 1]) and check[row - 1][col]:
                return ret
            elif col == 0 or check[row][col - 1]:
                go_up(row - 1, col)
            else:
                go_left(row, col - 1)

        def go_up(row, col):
            ret.append(matrix[row][col])
            check[row][col] = True
            if (row == 0 or check[row - 1][col]) and check[row][col + 1]:
                return ret
            elif row == 0 or check[row - 1][col]:
                go_right(row, col + 1)
            else:
                go_up(row - 1, col)

        def go_down(row, col):
            ret.append(matrix[row][col])
            check[row][col] = True
            if (row == m - 1 or check[row + 1][col]) and check[row][col - 1]:
                return ret
            elif row == m - 1 or check[row + 1][col]:
                go_left(row, col - 1)
            else:
                go_down(row + 1, col)

        go_right()
        return ret


if __name__ == '__main__':
    print(
        Solution().spiralOrder([[1, 2, 3, 4, 5]])
    )

```