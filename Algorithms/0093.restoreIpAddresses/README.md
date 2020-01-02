# 93. 复原IP地址

## 题意

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

**示例:**
```
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
```
## 题解

回溯。回溯时记录上一个放置的点以及待放置的点两个参数，每次检查从上一个点到目前位置的子串是否合法，如果合法则在当前位置放置该点，
并检查3个点是否都放好了，如果是的话则将结果添加到结果集里，否则放置下一个点。

## 标程

```python
from typing import List


class Solution(object):
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(now_s):
            return int(now_s) <= 255 if now_s[0] != "0" else len(now_s) == 1

        def update_output(curr_pos):
            segment = s[curr_pos + 1:len(s)]
            if check(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos=-1, dots=3):
            for i in range(prev_pos + 1, min(len(s) - 1, prev_pos + 4)):
                now_s = s[prev_pos + 1:i + 1]
                if check(now_s):
                    segments.append(now_s)
                    if dots - 1 == 0:
                        update_output(i)
                    else:
                        backtrack(i, dots - 1)
                    segments.pop()

        output, segments = [], []
        backtrack()
        return output


if __name__ == '__main__':
    print(
        Solution().restoreIpAddresses(
            "25525511135"
        )
    )

```