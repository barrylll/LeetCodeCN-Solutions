from typing import List


class Solution(object):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [dict() for _ in range(9)]
        rows = [dict() for _ in range(9)]
        boxes = [dict() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                box_index = (i // 3) * 3 + j // 3
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in boxes[box_index]:
                    return False
                else:
                    rows[i][board[i][j]] = 1
                    columns[j][board[i][j]] = 1
                    boxes[box_index][board[i][j]] = 1
        return True


if __name__ == '__main__':
    print(
        Solution().isValidSudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
])
    )
