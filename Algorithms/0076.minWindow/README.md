# 76. 最小覆盖子串

## 题意

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

**示例:**
```
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
```

**说明:**

1.  如果 S 中不存这样的子串，则返回空字符串 ""。
2.  如果 S 中存在这样的子串，我们保证它是唯一的答案。

## 题解

滑动窗口。定义两个指针`left`和`right`，先将`right`右移直到`left`和`right`中间的字符串能包含`t`中的所有元素，然后将`left`右移，
直到区间内不能包含`t`中的所有元素，每次记录这样的区间的最小值。

## 标程

```python
import collections


class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        dict_t = collections.Counter(t)
        left = right = 0
        temp = {}
        ans = (float("inf"), 0, 0)
        required = len(dict_t)
        in_window = 0
        while right < len(s):
            character = s[right]
            temp[character] = temp.get(character, 0) + 1
            if temp[character] == dict_t[character]:
                in_window += 1
            while left <= right and in_window == required:
                character = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                temp[character] -= 1
                if character in dict_t and temp[character] < dict_t[character]:
                    in_window -= 1
                left += 1
            right += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


if __name__ == '__main__':
    print(
        Solution().minWindow("ADOBECODEBANC", "ABC")
    )

```