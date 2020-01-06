# 96. 不同的二叉搜索树

## 题意

给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

**示例:**
```
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```
## 题解

动态规划。用`dp[i]`表示`i`个节点能组成的二叉搜索树的个数，`tree_num[i][j]`表示总共有`i`个节点时根节点为`j`的树的个数。
容易看出以`j`为根节点时，`j`的左子树有`j - 1`个节点，`j`的右子树有`i - j`个节点，那么此时以`j`为根节点的树的个数有`dp[j - 1] * dp[i - j]`个。
`dp[i]`即可由所有`j`求和取得。

## 标程

```python
class Solution(object):
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        tree_num = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                tree_num[i][j] = dp[j - 1] * dp[i - j]
                dp[i] += tree_num[i][j]
        return dp[n]


if __name__ == '__main__':
    print(
        Solution().numTrees(5)
    )

```