from typing import List


class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            index = -1
        else:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    index = mid
                    break
                elif nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        if index + 1 == 0:
            return self.Bsearch(nums, target)
        if target >= nums[0]:
            return self.Bsearch(nums[:index + 1], target)
        else:
            return index + 1 + self.Bsearch(nums[index + 1:], target) \
                if self.Bsearch(nums[index + 1:], target) != -1 else -1

    def Bsearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    print(
        Solution().search([6, 7, 8, 1, 2, 3, 4, 5], 6)
    )
