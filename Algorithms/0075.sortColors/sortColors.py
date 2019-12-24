from typing import List


class Solution(object):
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = left = 0
        right = len(nums) - 1
        while cur <= right:
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            elif nums[cur] == 1:
                cur += 1
        print(nums)


if __name__ == '__main__':
    print(
        Solution().sortColors([2, 0, 1])
    )
