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
