from typing import List

class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = set()
        for i in range(0, len(nums)):
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    temp.add((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
        ret = []
        for i in temp:
            ret.append(list(i))
        return ret

if __name__ == '__main__':
    print(
        Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
    )
