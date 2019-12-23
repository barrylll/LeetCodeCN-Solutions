# 72. 编辑距离

## 题意

给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

1.  插入一个字符
2.  删除一个字符
3.  替换一个字符

**示例1:**
```
输入: word1 = "horse", word2 = "ros"
输出: 3
解释: 
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```

**示例2:**
```
输入: word1 = "intention", word2 = "execution"
输出: 5
解释: 
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```
## 题解

动态规划。

对于`dp[i][j]`来说，他等于到他左边、上边、左上格子的最小操作数再进行一次操作，也就是这三个数的最小值加1。但是需要考虑到当
`word1[i] == word2[j]`时，此时的操作数相对于`dp[i - 1][j - 1]`没有改动，所以得到转移方程为：

```python
if word1[i - 1] == word2[j - 1]:
    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] - 1) + 1
else:
    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
```

## 标程

```python
class Solution(object):
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] - 1) + 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[len(word1)][len(word2)]


if __name__ == '__main__':
    print(
        Solution().minDistance("intention", "execution")
    )

```