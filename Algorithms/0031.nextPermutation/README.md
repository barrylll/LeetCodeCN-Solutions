# 30. 串联所有单词的子串

## 题意

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
```
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```
## 题解

举个例子说明，`[1, 2, 3, 5, 6, 4, 3, 1]`这个`list`的下一个排列是`[1, 2, 3, 6, 1, 3, 4, 5]`，那么容易看出来想要获得下一个排列需要三步：

1. 从右往左找，找到第一个满足`a[i] < a[i + 1]`的数。这个数就是需要往后交换的数。

2. 从右往左找，找到第一个满足`a[j] > a[i]`的数。这个数就是需要和`a[i]`交换的数。将这两个数交换。

3. 将`a[i + 1]`后面的数按照从小到大的顺序排列。按照我们前两步筛选的标准，容易知道`a[i + 1]`后面的数一定是从大到小排列的，所以这一步仅需将这些数顺序排列逆序即可。

## 标程

```python
from typing import List


class Solution(object):
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]
        print(nums)


if __name__ == '__main__':
    print(
        Solution().nextPermutation([1, 3, 2])
    )

```
