# 7. 整数反转

## 题意

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

**示例1**:

输入: 123

输出: 321

**示例2**:

输入: -123

输出: -321

**示例3**:

输入: 120

输出: 21

## 题解

用一个`str`把题目给出的整数从尾到头存储起来，再把`str`转化为整数类型输出，注意特判边界情况以及正负即可。

## 标程

```python
class Solution(object):
    def reverse(self, x: int) -> int:
        num = ""
        temp = abs(x)
        if temp == 0:
            return 0
        while temp != 0:
            n = temp % 10
            temp = temp // 10
            num = num + str(n)
        ret = int(num) if x >= 0 else -int(num)
        if ret > 2147483647 or ret < -2147483648:
            return 0
        else:
            return ret

if __name__ == '__main__':
    print(
        Solution().reverse(1463847412)
    )
```