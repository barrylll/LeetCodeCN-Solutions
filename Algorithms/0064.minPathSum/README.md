# 62. 不同路径

## 题意

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

**说明:**

每次只能向下或者向右移动一步。

**示例:**

```
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
```

## 题解

动态规划。

初始化`dp[i][0]`和`dp[0][j]`为这一行或这一列之前的所有数之和，`dp[i][j]`等于`dp[i - 1][j]`和`dp[i][j - 1]`中的较小值加上`grid[i][j]`。

## 标程

```python
from typing import List


class Solution(object):
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    print(
        Solution().minPathSum([
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ])
    )

```