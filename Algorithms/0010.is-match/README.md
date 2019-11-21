# 10. 正则表达式匹配

## 题意

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

```
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
```

所谓匹配，是要涵盖 **整个** 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。

p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 \*。

**示例1**:

输入:

s = "aa"

p = "a"

输出: false

解释: "a" 无法匹配 "aa" 整个字符串。

**示例2**:

输入:

s = "aa"

p = "a\*"

输出: true

解释: 因为 '\*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

**示例3**:

输入:

s = "ab"

p = ".*"

输出: true

解释: ".\*" 表示可匹配零个或多个（'\*'）任意字符（'.'）。

**示例4**:

输入:

s = "aab"

p = "c\*a\*b"

输出: true

解释: 因为 '\*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

**示例5**:

输入:

s = "mississippi"

p = "mis\*is\*p\*."

输出: false

## 题解

动态规划，用`dp[i][j]`表示`s[:i]`与`p[:j]`是否满足题目要求，根据`p[j]`可能存在的情况进行分析：

1.`p[j]`能直接与`s[i]`匹配

```
if p[j] == s[i] or p[j] == '.': 
    dp[i][j] = dp[i - 1][j - 1]
```

2.`p[j] == '*'`，则需要判断`p[j - 1]`是否能与`s[i]`匹配
    
(1).`p[j - 1]`能与`s[i]`匹配

```
if p[j - 1] == s[i] or p[j - 1] == '.':
    dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i][j - 2]
#dp[i][j] = dp[i - 1][j] 表示 * 匹配了多个字符	
#dp[i][j] = dp[i][j - 1] 表示 * 匹配了单个字符
#dp[i][j] = dp[i][j - 2] 表示 * 匹配了零个字符
```

(2).`p[j - 1]`不能与`s[i]`匹配

```
elif p[j - 1] != s[i]:
    dp[i][j] = dp[i][j - 2]
```

## 标程

```python
# -*- coding: utf-8 -*-

class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(30)] for _ in range(30)]
        dp[-1][-1] = True

        # 预处理，p 头部的 * 可以跟空串匹配
        for i in range(len(p)):
            if p[i] == '*' and dp[-1][i - 2]:
                dp[-1][i] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i][j - 2]
                    elif p[j - 1] != s[i]:
                        dp[i][j] = dp[i][j - 2]

        return dp[len(s) - 1][len(p) - 1]

if __name__ == '__main__':
    print(
        Solution().isMatch("aab", "c*a*b")
    )
```