# 90. 子集 II

## 题意

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

**说明：**

解集不能包含重复的子集。

**示例:**
```
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```
## 题解

参考[第78题](https://github.com/barrylll/LeetCodeCN-Solutions/tree/master/Algorithms/0078.subsets)，在往结果集里`append`的时候注意别`append`已经在结果集里的子集即可。

## 标程

```python
from typing import List


class Solution(object):
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
                    temp.sort()
                    if temp not in ret:
                        ret.append(temp)
                backtrack(now + 1)

        ret = []
        backtrack(-1)
        return ret


if __name__ == '__main__':
    output = [4, 4, 4, 1, 4]
    print(
        Solution().subsetsWithDup(output)
    )

```