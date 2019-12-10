from typing import List


class Solution(object):
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        ma = left = 0
        mi = right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                mi = min(mi, mid)
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ma = max(ma, mid)
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if ma == 0 and mi == len(nums) - 1:
            ma = mi = -1
        ret = [mi, ma]
        return ret


if __name__ == '__main__':
    print(
        Solution().searchRange([1], 1)
    )
