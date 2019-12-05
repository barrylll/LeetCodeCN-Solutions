# 25. K 个一组翻转链表

## 题意

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

**示例1**:

输入: dividend = 10, divisor = 3

输出: 3

**示例2**:

输入: dividend = 7, divisor = -3

输出: -2

**说明**:

被除数和除数均为 32 位有符号整数。

除数不为 0。

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。

## 题解

首先最简单的想法就是用减法，用被除数减去除数，直到被除数小于除数为止。但是这样的做法在边界情况会超时。

因此考虑将除法转换为二进制的减法。具体操作为，首先将除数左移，直到除数大于被除数，然后在每次循环时将除数右移并用被除数减去除数（如果被除数大于除数），同时结果加上此时除数相对于初始除数的倍数。

## 标程

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        left = abs(dividend)
        right = abs(divisor)
        ret = count = 0
        while left >= right:
            right <<= 1
            count += 1
        while count > 0:
            count -= 1
            right >>= 1
            if left >= right:
                ret += 1 << count
                left -= right
        if (dividend > 0) ^ (divisor > 0):
            ret = -ret
        if ret > 2**31 - 1 or ret < -2**31:
            return 2**31 - 1
        else:
            return ret

if __name__ == '__main__':
    print(
        Solution().divide(-2147483648, 1)
    )

```
