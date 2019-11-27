# 15. 三数之和

## 题意

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

```
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```
## 题解

因为涉及到3个可变的量，所以最简单的想法就是将这三个变量都进行循环，此时时间复杂度为`O(n^3)`。想要减少时间复杂度的方法就是使用双指针，对最小（或最大）的变量进行循环，假设循环变量是`i`，两个指针`left`和`right`分别指向`i + 1`和`len(nums) - 1`（或`i - 1`和`0`)，接下来对`nums[i] + nums[left] + nums[right]`进行判断，如果大于0则右指针左移，如果小于0则左指针右移，如果等于0则将该结果添加进结果集中。需要注意的是题目要求不能输出相同的三元组，所以会使用一个`set`来存储这些三元组，在输出时转换为`list`输出即可。

## 标程

```python
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
```