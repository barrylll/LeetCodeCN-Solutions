# 40. 组合总和 II

## 题意

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

1.  所有数字（包括 target）都是正整数。
2.  解集不能包含重复的组合。 


**示例1:**

```
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```
**示例2:**
```
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
```
## 题解

类似[第39题](https://github.com/hexsix/LeetCodeCN-Solutions/tree/master/Algorithms/0039.combinationSum)，区别在于本题要求`candidates`中的所有数都只能使用一次，因此在上一题的基础上在递归的过程中加入了`s`参数，默认等于`candidates`，在每次递归的时候在`s`中移除已经使用过的元素。

需要注意的是如果直接这么写的话会超时，因此做了两个剪枝，一是先将`candidates`排序后对`candidates`中的元素进行遍历，这样在遇到大于`target`的时候可以直接`break`；二是在遍历`candidates`的过程中，如果遇到前后两个相同的元素，那么这两个元素对应的返回结果一定是重复的，把这样的结果剪掉。

## 标程

```python
from typing import List

class Solution(object):
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from copy import deepcopy
        candidates.sort()

        def backtrack(tar, s=candidates):
            if tar == 0:
                return [[]]
            re = []
            for i in range(len(s)):
                if s[i] <= tar:
                    if i > 0 and s[i] == s[i - 1]:
                        continue
                    s_temp = deepcopy(s)
                    s_temp.pop(i)
                    for j in backtrack(tar - s[i], s_temp):
                        j.append(s[i])
                        re.append(j)
                else:
                    break
            return re

        temp = backtrack(target)
        ret = []
        for i in temp:
            i.sort()
            if i and i not in ret:
                ret.append(i)
        return ret


if __name__ == '__main__':
    print(
        Solution().combinationSum2([1,1,1,3,4], 7)
    )

```