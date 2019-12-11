# 39. 组合总和

## 题意

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

1.  所有数字（包括 target）都是正整数。
2.  解集不能包含重复的组合。 


**示例1:**

```
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
```
**示例2:**
```
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```
## 题解

递归。对于当前`target`，他的返回值等于遍历所有`i`的`target - candidates[i]`的所有返回值后面都加一个`candidates[i]`，然后对此结果取并集。

举个例子，对于输入`candidates = [2, 3, 4], target = 7`，`target`为`7`的返回值就等于`target`为`5`的返回值加`target`为`4`的返回值加`target`为`3`的返回值，而这些返回值又都可以递归往前得到。

## 标程

```python
from typing import List


class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(tar):
            if tar == 0:
                return [[]]
            re = []
            for i in candidates:
                if i <= tar:
                    for j in backtrack(tar - i):
                        j.append(i)
                        re.append(j)
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
        Solution().combinationSum([1, 2, 3, 4, 5], 6)
    )

```