# 60. 第k个排列

## 题意

给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"

"132"

"213"

"231"

"312"

"321"

给定 n 和 k，返回第 k 个排列。

**说明：**

给定 n 的范围是 [1, 9]。

给定 k 的范围是[1,  n!]。

**示例1:**

```
输入: n = 3, k = 3
输出: "213"
```
**示例2:**

```
输入: n = 4, k = 9
输出: "2314"
```

## 题解

递归。对于`n`个数的排列，可以分为`n`个组，每个组`(n - 1)!`个数。将`k // (n - 1)!`所得数就是在当前位应该放的数（需要注意如果整除的话应该算在上一组），然后递归求每一位应该放的数即可。

## 标程

```python
class Solution(object):
    def getPermutation(self, n: int, k: int) -> str:
        def cal_factorial(n):
            now = 1
            for i in range(n):
                now = now * (i + 1)
                factorial_num.append(now)

        def num_list(n):
            nums = []
            for i in range(n):
                nums.append(i + 1)
            return nums

        def backtrack(n, k, nums):
            div = factorial_num[n - 1]
            next_k = k % div
            group = k // div + (1 if next_k > 0 else 0) - 1
            temp = nums[group]
            nums.pop(group)
            if n - 1 > 0:
                return str(temp) + backtrack(n - 1, next_k, nums)
            else:
                return str(temp)

        factorial_num = [1]
        cal_factorial(n)
        return backtrack(n, k, num_list(n))


if __name__ == '__main__':
    print(
        Solution().getPermutation(3, 3)
    )

```