# 3. 无重复字符的最长子串

## 题意

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

**示例1**:

输入: "abcabcbb"

输出: 3 

解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

**示例2**:

输入: "bbbbb"

输出: 1

解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

**示例3**:

输入: "pwwkew"

输出: 3

解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

## 题解

滑动窗口，维护一个 `list` L，在遍历字符串的过程中将每一个字符都添加到 L 中，同时判断 `len(L)` 是否等于 `len(set(L))` (即 L 中是否有重复字符)，如果有则去掉 L 的第一位，直到 L 中没有重复字符，此时 L 的长度中的最大值就是最长子串的长度。

## 标程

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = []
        ret = 0
        for i in s:
            L.append(i)
            while len(L) != len(set(L)):
                L = L[1:]
            ret = max(ret, len(L))
        return ret

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
    print(Solution().lengthOfLongestSubstring('bbbb'))
    print(Solution().lengthOfLongestSubstring('pwwkew'))
```