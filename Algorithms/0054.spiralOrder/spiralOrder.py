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
