from typing import List


class Solution(object):
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True if nums[0] == target else False
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]:
                left += 1
                continue
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == '__main__':
    print(
        Solution().search([1, 3, 1, 1, 1], 3)
    )
