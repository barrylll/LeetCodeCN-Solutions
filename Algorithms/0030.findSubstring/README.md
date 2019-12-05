# 25. K 个一组翻转链表

## 题意

给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

**示例1**:

输入：

  s = "barfoothefoobarman",
  
  words = ["foo","bar"]
  
输出：[0,9]

解释：

从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。

输出的顺序不重要, [9,0] 也是有效答案。

**示例2**:

输入：

  s = "wordgoodgoodgoodbestword",
  
  words = ["word","good","best","word"]
  
输出：[]

## 题解

滑动窗口，每次需要判断的范围是`words`中所有字符串加起来的长度`all_size`，即每次仅需判断`all_size`长度的字符串中是否包含所有`words`中的字符串，用一个`dict`存储`words`，`key`是`words`中的字符串，`value`是字符串出现的次数。这样每次在判断时，在`s`中截取`words`中一个字符串长度的字符串，然后判断是否在`dict`中，如果存在则`value -= 1`，`value == 0`时删除这个`key`，如果不存在返回`False`，如果循环遍历完之后`dict`为空，则返回`True`。

## 标程

```python
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        if s == "" or words == []:
            return []
        one_size = len(words[0])
        all_size = len(words) * one_size
        words_map = dict()
        for i in words:
            if i not in words_map:
                words_map[i] = 1
            else:
                words_map[i] += 1
        for i in range(len(s) - all_size + 1):
            d = dict(words_map)
            if self.matchSubstring(s[i:i + all_size], d, one_size):
                ret.append(i)
        return ret

    def matchSubstring(self, s: str, d: dict, size: int):
        for i in range(0, len(s), size):
            key = s[i:i + size]
            if key in d:
                d[key] -= 1
                if d[key] == 0:
                    del d[key]
            else:
                return False
        if not d:
            return True


if __name__ == '__main__':
    print(
        Solution().findSubstring("aaaaa", ["a", "a", "a", "a", "a"])
    )
```
