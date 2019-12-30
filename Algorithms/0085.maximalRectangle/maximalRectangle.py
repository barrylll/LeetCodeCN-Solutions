from typing import List


class Solution(object):
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0
            max_area = max(max_area, self.cal(heights))
        return max_area

    def cal(self, heights: List[int]):
        ret = 0
        stack = [-1]
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                ret = max(ret, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            ret = max(ret, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return ret


if __name__ == '__main__':
    print(
        Solution().maximalRectangle(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]
            ]
        )
    )
