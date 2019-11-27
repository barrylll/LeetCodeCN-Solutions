# 18. 四数之和

## 题意

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

**示例**:

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：

[

  [-1,  0, 0, 1],
  
  [-2, -1, 1, 2],
  
  [-2,  0, 0, 2]
  
]

## 题解

双指针，题解参考[第15题](https://github.com/hexsix/LeetCodeCN-Solutions/tree/master/Algorithms/0015.three-sum)，在此基础上多加一层循环即可，剪枝的思路就是当在某个时刻四个数的和大于`target`的时候，那么再往后就必定仍然大于`target`，剪掉后面的部分即可。

## 标程

```python
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
```