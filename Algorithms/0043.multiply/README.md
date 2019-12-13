# 43. 字符串相乘

## 题意

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

**示例1:**

```
输入: num1 = "2", num2 = "3"
输出: "6"
```

**示例2:**

```
输入: num1 = "123", num2 = "456"
输出: "56088"
```

**说明:**

1.  num1 和 num2 的长度小于110。
2.  num1 和 num2 只包含数字 0-9。
3.  num1 和 num2 均不以零开头，除非是数字 0 本身。
4.  不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

## 题解

多位数乘法。模拟正常乘法的运算规则，首先模拟多位数和一位数相乘，然后模拟两个多位数的加法，对`num1`的每一位都和`num2`相乘，注意在结果后面加上对应位数的`"0"`，将所有结果两两进行多位数相加即可。

## 标程

```python
class Solution(object):
    def multiply(self, num1: str, num2: str) -> str:
        def single_mul(s, n):
            ret = ""
            up = 0
            s = s[::-1]
            for str_i in s:
                i = int(str_i)
                now = (i * n + up) % 10
                up = (i * n + up) // 10
                ret += str(now)
            if up > 0:
                ret += str(up)
            return ret[::-1]

        def two_sum(n1, n2):
            ret = ""
            if len(n2) >= len(n1):
                n2, n1 = n1, n2
            n1 = n1[::-1]
            n2 = n2[::-1]
            up = 0
            for i in range(len(n1)):
                if i < len(n2):
                    now = int(n1[i]) + int(n2[i]) + up
                    up = now // 10
                    now = now % 10
                    ret += str(now)
                else:
                    if up > 0:
                        now = int(n1[i]) + up
                        up = now // 10
                        now = now % 10
                        ret += str(now)
                    else:
                        ret += n1[i]
            if up > 0:
                ret = ret + str(up)
            return ret[::-1]

        if len(num2) >= len(num1):
            num2, num1 = num1, num2
        re = ""
        zeros = ""
        num2 = num2[::-1]
        for i in num2:
            re = two_sum(re, single_mul(num1, int(i)) + zeros)
            zeros += "0"
        if re[0] == "0" and len(re) > 1:
            re = "0"
        return re


if __name__ == '__main__':
    print(
        Solution().multiply("0", "43215")
    )

```