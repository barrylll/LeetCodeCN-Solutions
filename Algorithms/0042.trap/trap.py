from typing import List


class Solution(object):
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ret = 0
        l_line = [0 for _ in range(len(height))]
        r_line = [0 for _ in range(len(height))]
        l_line[0] = height[0]
        r_line[len(height) - 1] = height[len(height) - 1]
        for i in range(1, len(height)):
            l_line[i] = max(l_line[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            r_line[i] = max(r_line[i + 1], height[i])
        for i in range(len(height)):
            ret += min(r_line[i], l_line[i]) - height[i]
        return ret


if __name__ == '__main__':
    print(
        Solution().trap([2,2])
    )
