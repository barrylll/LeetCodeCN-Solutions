# 41. 缺失的第一个正数

## 题意

给定一个未排序的整数数组，找出其中没有出现的最小的正整数。


**示例1:**

```
输入: [1,2,0]
输出: 3
```
**示例2:**
```
输入: [3,4,-1,1]
输出: 2
```
**示例2:**
```
输入: [7,8,9,11,12]
输出: 1
```
## 题解

本题的关键在于对数组中每个数`index`和`value`建立关系，比较简单的一个想法是保证数组中每个数的`index = value - 1`，
即保证`nums[0] = 1, nums[1] = 2...nums[n] = n + 1`。这样在找满足条件的最小整数时只需从左遍历一遍，找到第一个不满足`nums[i] = i + 1`的数即可。
对数组建立上述关系的方法如下：

遍历一遍数组，如果`nums[i] <= 0 or nums[i] > len(nums)`，则认为这个位置存储的数对我们的输出没有意义，忽略。否则设这个位置存储的数为`value`，将`num[value - 1]`与`nums[i]`交换位置，这样就将`nums[value - 1]`处的数字存好了。这样遍历完整个数组就能保证数组已经按照上述规律进行了存储。

## 标程

```python
from typing import List


class Solution(object):
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == nums[nums[i] - 1]:
                    break
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

if __name__ == '__main__':
    print(
        Solution().firstMissingPositive([1, 2, 3, 6])
    )

```