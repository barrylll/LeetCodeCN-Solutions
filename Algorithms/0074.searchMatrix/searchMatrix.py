from typing import List


class Solution(object):
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right + 1) // 2
            index_row = mid // n
            index_col = mid % n
            if matrix[index_row][index_col] == target:
                return True
            elif matrix[index_row][index_col] > target:
                right = mid - 1
            elif matrix[index_row][index_col] < target:
                left = mid + 1
        return False


if __name__ == '__main__':
    print(
        Solution().searchMatrix([
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 13)
    )
