# 103. 二叉树的锯齿形层次遍历

## 题意

给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
返回锯齿形层次遍历如下：
```
[
  [3],
  [20,9],
  [15,7]
]
```

## 题解

参考[第102题](https://github.com/barrylll/LeetCodeCN-Solutions/tree/master/Algorithms/0102.levelOrder)。  
在输出时把奇数行反序输出即可。

## 标程

```python
from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        ret = []
        queue = []
        cur = self
        while cur or queue:
            val = cur.val if cur else None
            ret.append(val)
            if cur and (cur.left is not None or cur.right is not None):
                queue.append(cur.left)
                queue.append(cur.right)
            cur = queue.pop(0) if queue else None
        return str(ret)


class Solution(object):
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def backtrack(queue):
            nxt_queue, temp = [], []
            while queue:
                cur = queue.pop(0)
                temp.append(cur.val)
                if cur.left:
                    nxt_queue.append(cur.left)
                if cur.right:
                    nxt_queue.append(cur.right)
            if temp:
                ret.append(temp)
                backtrack(nxt_queue)

        if not root:
            return []
        ret = []
        backtrack([root])
        for i in range(len(ret)):
            if i % 2 == 1:
                ret[i] = ret[i][::-1]
        return ret


if __name__ == '__main__':
    print(
        Solution().zigzagLevelOrder(
            TreeNode(2, TreeNode(1), TreeNode(3))
        )
    )

```