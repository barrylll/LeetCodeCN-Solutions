from typing import List

class Solution(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mi = float("inf")
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = abs(nums[i] + nums[left] + nums[right] - target)
                if temp < mi:
                    ret = nums[i] + nums[left] + nums[right]
                    mi = temp
                if nums[i] + nums[left] + nums[right] - target >= 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] - target < 0:
                    left += 1
        return ret

if __name__ == '__main__':
    print(
        Solution().threeSumClosest([-1, 2, 1, -4], 1)
    )
