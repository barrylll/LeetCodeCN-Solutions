# 120. 三角形最小路径和

## 题意

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

**说明：**

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

## 题解

如果空间没有要求的话，DP的思路很清晰，`dp[i][j]`表示到达`(i, j)`位置的最小值，
那么`dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]`。

但是题目要求要用O(n)的额外空间，可以注意到动态规划转移方程只跟相邻的两行有关，即`i`只跟`i - 1`有关，与之前的无关，
于是可以考虑只用两个一维数组来交替进行状态转移。

但是其实如果将`j`从`i - 1`开始递减到`0`，可以再省去一个一维数组，因为这样每次计算后的结果不会影响到接下来的计算。

## 标程

```python
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = triangle[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
            dp[0] += triangle[i][0]
        ret = min(dp)
        return ret


if __name__ == '__main__':
    print(
        Solution().minimumTotal(
            [
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
            ]
        )
    )

```