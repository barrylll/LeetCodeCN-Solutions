from typing import List


class Solution(object):
    def canJump(self, nums: List[int]) -> bool:
        max_range = nums[0]
        for i in range(len(nums)):
            if i > max_range:
                return False
            max_range = max(max_range, i + nums[i])
        return True


if __name__ == '__main__':
    print(
        Solution().canJump([1, 2, 3, 4, 5])
    )
