# 77. 组合

## 题意

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

**示例:**
```
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```
## 题解

回溯。用一个数组`num`存储当前的组合，从`1`开始往`n`遍历，同时添加进`num`内。如果`num`的长度等于`k`则添加进输出里，否则回溯。

## 标程

```python
from typing import List


class Solution(object):
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(now, num):
            if len(num) == k:
                ret.append(num[:])
            for i in range(now, n + 1):
                num.append(i)
                backtrack(i + 1, num)
                num.pop()

        ret = []
        backtrack(1, [])
        return ret


if __name__ == '__main__':
    print(
        Solution().combine(4, 2)
    )

```