# 89. 格雷编码

## 题意

格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

**示例1:**
```
输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
```

**示例2:**
```
输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。
```

## 题解

递归。从`n`到`n - 1`时，因为知道`n - 1`都是按照顺序排列的，所以将`n - 1`的所有结果在最首位加一个`1`（二进制下），加上原来`n - 1`的结果，所得的就是`n`的结果。

## 标程

```python
from typing import List


class Solution(object):
    def grayCode(self, n: int) -> List[int]:
        def backtrack(num):
            if num == 0:
                return ["0"]
            if num == 1:
                return ["0", "1"]
            pre = backtrack(num - 1)
            ret = pre[:]
            for i in range(len(pre) - 1, -1, -1):
                temp = "1" + "0" * (num - 1 - len(pre[i])) + pre[i]
                ret.append(temp)
            return ret

        res = []
        for i in backtrack(n):
            res.append(int(i, 2))
        return res


if __name__ == '__main__':
    print(
        Solution().grayCode(4)
    )

```