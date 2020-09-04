# 257. 二叉树的所有路径

## 题意

给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

**示例：**

```
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

```


## 题解

深度优先遍历，递归。

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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def Rec(root, path):
            if root:
                path += str(root.val)
                if root.left is None and root.right is None:
                    ret.append(path)
                else:
                    path += "->"
                    Rec(root.left, path)
                    Rec(root.right, path)

        ret = []
        Rec(root, "")
        return ret


if __name__ == '__main__':
    print(
        Solution().binaryTreePaths(
            TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
        )
    )

```