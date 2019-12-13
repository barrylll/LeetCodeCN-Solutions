# 44. 通配符匹配

## 题意

给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
```
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
```
两个字符串完全匹配才算匹配成功。

**说明:**

1.  s 可能为空，且只包含从 a-z 的小写字母。
2.  p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

**示例1:**

```
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
```

**示例2:**

```
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
```

**示例3:**

```
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
```

**示例4:**

```
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
```

**示例5:**

```
输入:
s = "acdcb"
p = "a*c?b"
输入: false
```


## 题解

动态规划。参考[第10题](https://github.com/hexsix/LeetCodeCN-Solutions/tree/master/Algorithms/0010.is-match)，用`dp[i][j]`表示`s[:i]`与`p[:j]`是否满足题目要求，根据`p[j]`可能存在的情况进行分析：

如果`p[j - 1] == s[i - 1]`或`p[j - 1] == '?'`，那么这一位已经可以匹配，`dp[i][j] = dp[i - 1][j - 1]`

如果`p[j - 1] == '*'`，那么`"*"`可能匹配0个或多个字符，即`dp[i][j] = dp[i][j - 1] or dp[i - 1][j]`，其中`dp[i][j] = dp[i][j - 1]`表示匹配0个字符，`dp[i][j] = dp[i - 1][j]`表示匹配多个字符。


## 标程

```python
class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[len(s)][len(p)]


if __name__ == '__main__':
    print(
        Solution().isMatch("abc", "???")
    )

```