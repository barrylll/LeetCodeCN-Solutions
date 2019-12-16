# 49. 字母异位词分组

## 题意

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

**示例:**

```
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```
**说明:**
1.  所有输入均为小写字母。
2.  不考虑答案输出的顺序。

## 题解

维护一个`dict`，`key`是`strs`中`sort`之后的元素，`value`是这个元素对应在返回值中的`index`。遍历`strs`，检查如果在`dict`中已有则加到对应`index`的`list`中，否则新建一个`list`。

## 标程

```python
from typing import List


class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        check = {}
        cnt = 0
        for i in strs:
            temp = list(i)
            temp.sort()
            if str(temp) not in check:
                to_be_append = [i]
                ret.append(to_be_append)
                check[str(temp)] = cnt
                cnt += 1
            else:
                temp = list(i)
                temp.sort()
                ret[check[str(temp)]].append(i)
        return ret


if __name__ == '__main__':
    print(
        Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    )

```