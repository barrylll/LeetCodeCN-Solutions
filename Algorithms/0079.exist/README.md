# 77. 组合

## 题意

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

**示例:**
```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
```
## 题解

递归。维护一个`now_idx`表示当前已经找到第几位，如果`now_idx`为`0`则遍历整个表，找到能匹配第一个字母的位置，从这个位置开始向上、向下、向左、向右遍历，直到匹配到所有的字母为止。

## 标程

```python
from typing import List


class Solution(object):
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def visit(pos_i, pos_j, now_idx):
            if 0 <= pos_j < n and 0 <= pos_i < m and not visited[pos_i][pos_j] and board[pos_i][pos_j] == word[now_idx]:
                visited[pos_i][pos_j] = True
                if search(pos_i, pos_j, now_idx + 1):
                    return True
                visited[pos_i][pos_j] = False

        def search(pos_i=0, pos_j=0, now_idx=0):
            if now_idx == 0:
                for i in range(m):
                    for j in range(n):
                        if board[i][j] == word[now_idx]:
                            visited[i][j] = True
                            if search(i, j, now_idx + 1):
                                return True
                            visited[i][j] = False
            elif now_idx == len(word):
                return True
            else:
                if visit(pos_i, pos_j + 1, now_idx) or visit(pos_i, pos_j - 1, now_idx) or \
                        visit(pos_i + 1, pos_j, now_idx) or visit(pos_i - 1, pos_j, now_idx):
                    return True
            return False

        return search()


if __name__ == '__main__':
    print(
        Solution().exist([
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ], "ABCB")
    )

```