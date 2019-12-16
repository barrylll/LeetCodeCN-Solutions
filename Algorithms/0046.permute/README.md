# 46. 全排列

## 题意

给定一个没有重复数字的序列，返回其所有可能的全排列。

**示例:**

```
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## 题解

递归，每次递归时记录当前已经全排列好的数组和剩下待排列的数组，每次从待排列的数组中取一个数放到已排列好的数组末尾。

## 标程

```python
from typing import List


class Solution(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        from copy import deepcopy
        ret = []

        def backtrack(now, num):
            if not num:
                if len(now) > 0:
                    ret.append(now)
            else:
                for i in num:
                    nxt_num = deepcopy(num)
                    nxt_num.remove(i)
                    nxt_now = deepcopy(now)
                    nxt_now.append(i)
                    backtrack(nxt_now, nxt_num)

        backtrack([], nums)
        return ret


if __name__ == '__main__':
    print(
        Solution().permute([111, 222, 3333, 666])
    )

```