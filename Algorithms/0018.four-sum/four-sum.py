from typing import List

class Solution(object):
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        temp = set()
        for i in range(len(nums) - 3):
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            for j in range(i + 1, len(nums) - 2):
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        temp.add((nums[i], nums[j], nums[left], nums[right]))
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
        ret = []
        for i in temp:
            ret.append(list(i))
        return ret

if __name__ == '__main__':
    print(
        Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    )
