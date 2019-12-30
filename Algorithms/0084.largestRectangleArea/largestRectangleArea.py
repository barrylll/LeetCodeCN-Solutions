from typing import List


class Solution(object):
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ret = 0
        stack = [-1]
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                ret = max(ret, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            ret = max(ret, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return ret


if __name__ == '__main__':
    print(
        Solution().largestRectangleArea(
            [4, 2, 0, 3, 2, 4, 3, 4]
        )
    )
