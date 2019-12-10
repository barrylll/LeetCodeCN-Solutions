# 37. 解数独

## 题意

编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

1.  数字 1-9 在每一行只能出现一次。
2.  数字 1-9 在每一列只能出现一次。
3.  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

![<Sudoku>](<http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png>)

一个数独

![<Sudoku>](<http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png>)

答案被标成红色

Note:

1.  给定的数独序列只包含数字 1-9 和字符 '.' 。
2.  你可以假设给定的数独只有唯一解。
3.  给定数独永远是 9x9 形式的。

## 题解

判断数独是否合法的方法可以参考[第36题](https://github.com/hexsix/LeetCodeCN-Solutions/tree/master/Algorithms/0036.isValidSudoku)。

本题采用回溯的思想，在每个空位置放入`1~9`的同时判断是否合法，如果在某个位置放不下任何数了，则在这个位置往前回溯，直到所有空位置都能放下一个数字。此时所获得的解就是该数独问题的解。

## 标程

```python
from typing import List


class Solution(object):
    def solveSudoku(self, board: List[List[str]]) -> None:
        columns = [dict() for _ in range(9)]
        rows = [dict() for _ in range(9)]
        boxes = [dict() for _ in range(9)]
        solved = False

        def box_index(row, col):
            return (row // 3) * 3 + col // 3

        def check(val, row, col):
            if val in rows[row] or val in columns[col] or val in boxes[box_index(row, col)]:
                return False
            else:
                return True

        def add(val, row, col):
            board[row][col] = val
            rows[row][val] = 1
            columns[col][val] = 1
            boxes[box_index(row, col)][val] = 1

        def remove(val, row, col):
            board[row][col] = "."
            rows[row].pop(val)
            columns[col].pop(val)
            boxes[box_index(row, col)].pop(val)

        def add_rest(row, col):
            if row == 8 and col == 8:
                nonlocal solved
                solved = True
            else:
                if col == 8:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == ".":
                for i in range(1, 10):
                    if check(str(i), row, col):
                        add(str(i), row, col)
                        add_rest(row, col)
                        if not solved:
                            remove(str(i), row, col)
            else:
                add_rest(row, col)

        for i in range(9):
            for j in range(9):
                add(board[i][j], i, j)
        backtrack()
        print(board)

if __name__ == '__main__':
    print(
        Solution().solveSudoku([
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "8", ".", "1", ".", "5", ".", "4", "."],
            ["5", ".", ".", "4", ".", "9", "7", ".", "."],
            [".", ".", "1", ".", ".", ".", ".", ".", "8"],
            [".", ".", ".", "8", ".", "1", ".", ".", "."],
            ["3", ".", ".", ".", ".", ".", "1", ".", "."],
            [".", ".", "9", "7", ".", "2", ".", ".", "3"],
            [".", "6", ".", "5", ".", "8", ".", "1", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]
        ])
    )

```