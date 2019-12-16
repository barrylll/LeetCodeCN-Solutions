# 50. Pow(x, n)

## 题意

实现 pow(x, n) ，即计算 x 的 n 次幂函数。

**示例1:**

```
输入: 2.00000, 10
输出: 1024.00000
```

**示例2:**

```
输入: 2.10000, 3
输出: 9.26100
```

**示例3:**

```
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
```

**说明:**
1.  -100.0 < x < 100.0
2.  n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。

## 题解

快速幂。`x^n = x^n/2 * x^n/2`。每次计算的时候都递归计算`n/2`的结果，`n == 0`时返回1。

## 标程

```python
class Solution(object):
    def myPow(self, x: float, n: int) -> float:
        def backtrack(x, n):
            if n == 0:
                return 1
            elif n % 2 == 1:
                return x * (backtrack(x, n // 2) ** 2)
            else:
                return backtrack(x, n // 2) ** 2

        if n >= 0:
            return backtrack(x, n)
        else:
            return backtrack(1/x, -n)


if __name__ == '__main__':
    print(
        Solution().myPow(0.00001, 2147483647)
    )

```