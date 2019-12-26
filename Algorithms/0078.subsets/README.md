# 77. 组合

## 题意

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

**说明：**

解集不能包含重复的子集。

**示例:**
```
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```
## 题解

抱着T一发的态度交了一发，没想到过了...

递归。对于原数组中的每个元素，每次都遍历上一次结果并对结果中的所有元素都`append`一个当前值。

## 标程

```python
from typing import List


class Solution(object):
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(now):
            if now == -1:
                ret.append([])
                backtrack(now + 1)
            else:
                if now == len(nums):
                    return
                for i in ret[:]:
                    temp = i[:]
                    temp.append(nums[now])
                    ret.append(temp)
                backtrack(now + 1)

        ret = []
        backtrack(-1)
        return ret


if __name__ == '__main__':
    output = [i + 1 for i in range(10)]
    print(
        Solution().subsets(output)
    )

```