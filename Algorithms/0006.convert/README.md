# 6. Z字形变换

## 题意

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
```
L   C   I   R
E T O E S I I G
E   D   H   N
```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：
```
string convert(string s, int numRows);
```

**示例**:

输入: s = "LEETCODEISHIRING", numRows = 3

输出: "LCIRETOESIIGEDHN"

## 题解

找规律。容易发现当行数为`n`时，字符串内的字符位置每经过`2 * (n - 1)`会回到原点，而模`2 * (n - 1)`余`i`和余`2 * (n - 1) - i`的字符都会在同一行，将原字符串按照模`2 * (n - 1)`的余数排列即可。

## 标程

```python
class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            ret = [""] * numRows
            mod = 2 * (numRows - 1)
            for i in range(len(s)):
                t = i % mod
                if t < numRows:
                    ret[t] = ret[t] + s[i]
                else:
                    ret[mod - t] = ret[mod - t] + s[i]
            return "".join(ret)

if __name__ == '__main__':
    print(
        Solution().convert("LEETCODEISHIRING", 3)
    )
```