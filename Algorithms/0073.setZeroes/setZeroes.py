from typing import List


class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row = 1
        first_column = 1

        for i in range(m):
            if matrix[i][0] == 0:
                first_column = 0

        for j in range(n):
            if matrix[0][j] == 0:
                first_row = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_column == 0:
            for i in range(m):
                matrix[i][0] = 0
        if first_row == 0:
            for j in range(n):
                matrix[0][j] = 0
        print(matrix)


if __name__ == '__main__':
    print(
        Solution().setZeroes([
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ])
    )
