# 9. 回文数

## 题意

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

**示例1**:

输入: 121

输出: true

**示例2**:

输入: -121

输出: false

解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

**示例3**:

输入: 10

输出: false

解释: 从右向左读, 为 01 。因此它不是一个回文数。


## 题解

一个比较简单的思路就是把数字转换为字符串，把字符串逆序后对比判断是否相同。标程是一种不使用字符串的方法：

容易发现，所有的负数都一定不是回文数，对于正数来说，判断一个数是否为回文数就只需要判断这个数从左到右的每一位是否和从右到左的每一位相等，比如判断`1221`是否为回文数只需判断`(1221 // 1000 == 1221 % 10) and (22 // 10 == 22 & 10)`

## 标程

```python
class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            div = 1
            while x // div >= 10:
                div = div * 10
            while x > 0:
                left = x // div
                right = x % 10
                if left != right:
                    return False
                else:
                    x = x % div
                    x = x // 10
                    div = div // 100
            return True

if __name__ == '__main__':
    print(
        Solution().isPalindrome(1001)
    )
```