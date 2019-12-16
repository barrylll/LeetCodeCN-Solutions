# 46. 全排列

## 题意

给定一个可包含重复数字的序列，返回所有不重复的全排列。

**示例:**

```
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

## 题解

递归，思路参考[第46题](https://github.com/hexsix/LeetCodeCN-Solutions/tree/master/Algorithms/0046.permute)。
区别在于本题可能会出现相同的元素，所以需要在往`ret`里面`append`元素的时候注意判断一下`ret`里面是否已经有这个元素了。
但是这样直接提交会超时，剪枝的方法就是先对原始数组进行排序，然后在每次回溯的时候判断当前元素是否在之前已经计算过了，如果已经计算过了则不需继续计算，跳过即可。

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