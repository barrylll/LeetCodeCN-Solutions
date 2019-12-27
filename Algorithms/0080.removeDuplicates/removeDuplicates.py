from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1, 1, -1):
            if nums[i] == nums[i - 2]:
                nums.pop(i)
        return len(nums)


if __name__ == '__main__':
    print(
        Solution().removeDuplicates([1, 1, 1, 1, 1, 1])
    )
