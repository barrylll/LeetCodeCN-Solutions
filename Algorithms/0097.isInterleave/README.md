# 96. 不同的二叉搜索树

## 题意

给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

**示例1:**
```
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
```
**示例2:**
```
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
```
## 题解

动态规划。用`dp[i][j]`表示`s1`的前`i`位和`s2`的前`j`位能否和`s3`的前`i + j`位匹配。那么如果`dp[i - 1][j]`
或`dp[i][j - 1]`为`True`且`s1[i]`或`s2[j]`能与`s3[i + j]`匹配，`dp[i][j]`即为`True`。

## 标程

```python
class Solution(object):
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == j == 0:
                    dp[i][j] = True
                else:
                    if (j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) \
                            or (i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]):
                        dp[i][j] = True
        return dp[len(s1)][len(s2)]


if __name__ == '__main__':
    print(
        Solution().isInterleave("a", "", "a")
    )

```