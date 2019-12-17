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
