# 32. 最长有效括号

## 题意

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

**示例1:**

输入: "(()"

输出: 2

解释: 最长有效括号子串为 "()"

**示例2:**

输入: ")()())"

输出: 4

解释: 最长有效括号子串为 "()()"

## 题解

动态规划。维护一个数组`max_sub_len`表示在某个位置时往前数所能数到的最长子串的长度。如对于`"(((()()()()"`：`max_sub_len[5] = 2`、`max_sub_len[7] = 4`。

对于在某个位置`i`，如果`s[i] == "("`，那么这个位置的`max_sub_len[i]`就是没有意义的，设为默认值`0`。

如果`s[i] == ")"`，此时判断`s[i - 1]`：

如果`s[i - 1] == "("`，那么`s[i]`和`s[i - 1]`刚好组成了一个合法的括号对`"()"`，`max_sub_len[i] = max_sub_len[i - 2] + 2`；

如果`s[i - 1] == "("`，那么`s[i]`和`s[i - 1]`组成了`"))"`，此时需要判断`s[i - max_sub_len[i - 1] - 1]`，即在上一个最长子串的前一位是否有`"("`与`s[i]`匹配，如果有，那么就此处的`max_sub_len[i]`值就等于`max_sub_len[i - 1] + max_sub_len[i - max_sub_len[i - 1] - 2] + 2`。

## 标程

```python
class Solution(object):
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        max_sub_len = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ")" and s[i - 1] == "(":
                max_sub_len[i] = max_sub_len[i - 2] + 2
            elif s[i] == ")" and s[i - 1] == ")":
                if i - max_sub_len[i - 1] > 0 and s[i - max_sub_len[i - 1] - 1] == "(":
                    max_sub_len[i] = max_sub_len[i - 1] + ((max_sub_len[i - max_sub_len[i - 1] - 2]
                                                            if i - max_sub_len[i - 1] >= 2 else 0) + 2)
        return max(max_sub_len)


if __name__ == '__main__':
    print(
        Solution().longestValidParentheses("()()()(((()")
    )

```