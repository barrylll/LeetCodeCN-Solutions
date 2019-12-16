from typing import List


class Solution(object):
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        moved = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not moved[i][j] and not moved[n - j - 1][i] and not moved[n - i - 1][n - j - 1] and not moved[j][n - i - 1]:
                    matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = \
                        matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
                    moved[i][j] = moved[n - j - 1][i] = moved[n - i - 1][n - j - 1] = moved[j][n - i - 1] = True
        print(matrix)


if __name__ == '__main__':
    print(
        Solution().rotate([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
    )
