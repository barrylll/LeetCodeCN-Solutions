from typing import List

class Solution(object):
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cnt = i = 0
        while i < len(nums):
            if i + nums[i] + 1 >= len(nums):
                return cnt + 1
            else:
                ma = 0
                for j in range(i + 1, i + nums[i] + 1):
                    if nums[j] + j - i >= ma:
                        ma = nums[j] + j - i
                        nex = j
                i = nex
                cnt += 1


if __name__ == '__main__':
    print(
        Solution().jump([10,9,8,7,6,5,4,3,2,1,1,0])
    )
