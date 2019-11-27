# 12. 整数转罗马数字

## 题意

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![<phone>](<https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png>)

**示例**:

输入："23"

输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## 题解

递归，每个能输出的字符串相当于`digits[0]`代表的所有字符分别加上`digits[1:]`代表的字符串

## 标程

```python
from typing import List

class Solution(object):
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
               "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        ret = []

        def combine(combination, digits_):
            if digits_ == "":
                if len(combination) > 0:
                    ret.append(combination)
            else:
                for i in dic[digits_[0]]:
                    combine(combination + i, digits_[1:])

        combine("", digits)
        return ret

if __name__ == '__main__':
    print(
        Solution().letterCombinations("23")
    )
```

## 题解 2

用 `itertools` 里的 `product` 函数作笛卡尔乘积

## 标程 2

```python
from typing import List

class Solution(object):
    def letterCombinations(self, digits: str) -> List[str]:
        import itertools
        from functools import reduce
        
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        def my_product(a, b):
            return tuple(map(''.join, itertools.product(a, b)))

        if digits == '':
            return []
        else:
            return list(reduce(my_product, [dic[i] for i in digits]))
        
if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
```

