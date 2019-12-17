# 52. N皇后II

## 题意

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

![<Queen_map>](<https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png>)

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

**示例:**

```
输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
```
## 题解

参考[第51题](https://github.com/hexsix/LeetCodeCN-Solutions/tree/master/Algorithms/0051.solveNQueens).

## 标程

```python
class Solution(object):
    def totalNQueens(self, n: int) -> int:
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
        return len(ret)


if __name__ == '__main__':
    print(
        Solution().totalNQueens(4)
    )

```