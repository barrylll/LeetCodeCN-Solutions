# 51. N皇后

## 题意

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

![<Queen_map>](<https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png>)

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

**示例:**

```
输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
```
## 题解

回溯法。递归每一行，对于每一行都遍历一遍所有列，如果可以放皇后就在这个位置放一个皇后，否则往回退，每次退的时候收走之前放过的皇后。

## 标程

```python
from typing import List


class Solution(object):
    def solveNQueens(self, n: int) -> List[List[str]]:
        can_place_row = [True for _ in range(n)]
        can_place_col = [True for _ in range(n)]
        can_place_Mdia = [True for _ in range(2 * n)]
        can_place_Sdia = [True for _ in range(2 * n)]
        position = {}
        ret = []

        def place_Queen(row, col):
            can_place_row[row] = False
            can_place_col[col] = False
            can_place_Mdia[row + col] = False
            can_place_Sdia[row - col + n] = False
            position[row] = col

        def remove_Queen(row, col):
            can_place_row[row] = True
            can_place_col[col] = True
            can_place_Mdia[row + col] = True
            can_place_Sdia[row - col + n] = True
            del position[row]

        def can_place(row, col):
            return can_place_row[row] and can_place_col[col] and can_place_Mdia[row + col] and can_place_Sdia[row - col + n]

        def backtrack(row=0):
            for col in range(n):
                if can_place(row, col):
                    place_Queen(row, col)
                    if row == n - 1:
                        temp = ["" for _ in range(n)]
                        for r in position:
                            temp[r] += "." * position[r] + "Q" + "." * (n - position[r] - 1)
                        ret.append(temp)
                    else:
                        backtrack(row + 1)
                    remove_Queen(row, col)

        backtrack()
        return ret


if __name__ == '__main__':
    print(
        Solution().solveNQueens(4)
    )

```