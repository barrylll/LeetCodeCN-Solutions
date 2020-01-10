# 115. 不同的子序列

## 题意

给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

**示例1：**
```
输入: S = "rabbbit", T = "rabbit"
输出: 3
解释:

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
```
**示例2：**
```
输入: S = "babgbag", T = "bag"
输出: 5
解释:

如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
```

## 题解

动态规划。  
如果`s[i] == t[j]`，那么`dp[i][j]`由两部分组成，一部分是将`s[i]`和`t[j]`都参与到字符串匹配的过程中，这种情况的匹配个数为`dp[i - 1][j - 1]`，另一部分是`s[i]`不参与到字符串匹配的过程中，这种情况的匹配个数为`dp[i - 1][j]`，这样`dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]`。  
如果`s[i] != t[j]`，`s[i]`不能参与匹配，那么`dp[i][j] = dp[i - 1][j]`。

## 标程

```python
class Solution(object):
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s)):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(s)][len(t)]


if __name__ == '__main__':
    print(
        Solution().numDistinct(
            "babgbag", "bag"
        )
    )

```