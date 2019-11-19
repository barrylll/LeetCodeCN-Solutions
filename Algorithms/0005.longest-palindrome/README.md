# 5. 最长回文子串

## 题意

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

**示例1**:

输入: "babad"

输出: "bab"

注意: "aba" 也是一个有效答案。

**示例2**:

输入: "cbbd"

输出: "bb"

## 题解

动态规划

用`dp[i][j]`表示字符串`s`从`i`到`j`的子串是否为回文串，那么有：
```
dp[i][i] = True
dp[i][i + 1] = (s[i] == s[i + 1])
```
如果某个长度大于2的子串是回文串，则必满足：
```
dp[i + 1][j - 1] == True and s[i] == s[j]
```
由此可得状态转移方程
```
dp[i][j] = (s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]))
```

## 标程

```python
# -*- coding: utf-8 -*-
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        ma = -1
        ret = ""
        # 初始化
        for i in range(0, len(s)):
            dp[i][i] = True
            if i < len(s) - 1:
                dp[i][i + 1] = (s[i] == s[i + 1])
        for j in range(0, len(s)):
            for i in range(0, j + 1):
                dp[i][j] = (s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]))
                if dp[i][j] and j - i > ma:
                    ma = j - i
                    ret = s[i:j + 1]
        return ret



if __name__ == '__main__':
    print(
        Solution().longestPalindrome("dabab"),
        Solution().longestPalindrome("a"),
        Solution().longestPalindrome("")
    )
```