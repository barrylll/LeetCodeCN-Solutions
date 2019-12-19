# 59. 螺旋矩阵II

## 题意

给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

**示例1:**

```
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```

## 题解

参考[第54题](https://github.com/hexsix/LeetCodeCN-Solutions/tree/master/Algorithms/0054.spiralOrder)。

在遍历的过程中每次增加的元素从1开始递增即可。

## 标程

```python
from typing import List


class Solution(object):
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0 for _ in range(n)] for _ in range(n)]
        check = [[False for _ in range(n)] for _ in range(n)]

        def go_right(row=0, col=0, now=1):
            ret[row][col] = now
            now += 1
            check[row][col] = True
            if (col == n - 1 or check[row][col + 1]) and (row == n - 1 or check[row + 1][col]):
                return ret
            elif col == n - 1 or check[row][col + 1]:
                go_down(row + 1, col, now)
            else:
                go_right(row, col + 1, now)

        def go_left(row, col, now):
            ret[row][col] = now
            now += 1
            check[row][col] = True
            if (col == 0 or check[row][col - 1]) and check[row - 1][col]:
                return ret
            elif col == 0 or check[row][col - 1]:
                go_up(row - 1, col, now)
            else:
                go_left(row, col - 1, now)

        def go_up(row, col, now):
            ret[row][col] = now
            now += 1
            check[row][col] = True
            if (row == 0 or check[row - 1][col]) and check[row][col + 1]:
                return ret
            elif row == 0 or check[row - 1][col]:
                go_right(row, col + 1, now)
            else:
                go_up(row - 1, col, now)

        def go_down(row, col, now):
            ret[row][col] = now
            now += 1
            check[row][col] = True
            if (row == n - 1 or check[row + 1][col]) and check[row][col - 1]:
                return ret
            elif row == n - 1 or check[row + 1][col]:
                go_left(row, col - 1, now)
            else:
                go_down(row + 1, col, now)

        go_right()
        return ret


if __name__ == '__main__':
    print(
        Solution().generateMatrix(4)
    )

```