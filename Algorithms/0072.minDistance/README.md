# 71. 简化路径

## 题意

以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：[Linux / Unix中的绝对路径 vs 相对路径](https://blog.csdn.net/u011327334/article/details/50355600)

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

**示例1:**
```
输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。
```

**示例2:**
```
输入："/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
```

**示例3:**
```
输入："/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
```

**示例4:**
```
输入："/a/./b/../../c/"
输出："/c"
```

**示例5:**
```
输入："/a/../../b/../c//.//"
输出："/c"
```

**示例6:**
```
输入："/a//b////c/d//././/.."
输出："/a/b/c"
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