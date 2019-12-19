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
