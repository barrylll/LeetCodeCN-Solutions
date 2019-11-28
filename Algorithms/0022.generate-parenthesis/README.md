# 22. 括号生成

## 题意

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## 题解

递归。维护两个值`left`和`right`分别表示左括号的数量和右括号的数量，递归时先判断如果`left`小于`n`则可以加一个左括号，再判断如果`right`小于`left`则加一个右括号，这样能保证每次递归时的括号都是合法的。

## 标程

```python
from typing import List


class Solution(object):
    def generateParenthesis(self, n: int) -> List[str]:
        temp = set()

        def generater(generation="", left=0, right=0):
            if len(generation) == 2 * n:
                temp.add(generation)
            if left < n:
                generater(generation + "(", left + 1, right)
            if right < left:
                generater(generation + ")", left, right + 1)

        ret = []
        generater()
        for i in temp:
            ret.append(str(i))
        return ret


if __name__ == '__main__':
    print(
        Solution().generateParenthesis(4)
    )
```