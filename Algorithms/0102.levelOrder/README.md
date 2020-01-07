# 102. 二叉树的层次遍历

## 题意

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
返回其层次遍历结果：
```
[
  [3],
  [9,20],
  [15,7]
]
```

## 题解

BFS+递归。遍历每一层的时候都新建一个队列，把下一层的所有节点都放到队列内，然后遍历新的队列。

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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return ret


if __name__ == '__main__':
    print(
        Solution().levelOrder(
            TreeNode(2, TreeNode(1), TreeNode(3))
        )
    )

```