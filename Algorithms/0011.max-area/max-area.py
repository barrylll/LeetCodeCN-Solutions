from typing import List

class Solution(object):
    def maxArea(self, height: List[int]) -> int:
        ret = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[right], height[left])
            ret = max(ret, area)
            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1
        return ret

if __name__ == '__main__':
    print(
        Solution().maxArea([2, 2])
    )
