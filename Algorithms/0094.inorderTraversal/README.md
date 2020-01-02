# 94. 二叉树的中序遍历

## 题意

给定一个二叉树，返回它的中序 遍历。

**示例:**
```
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
```
**进阶：** 递归算法很简单，你可以通过迭代算法完成吗？
## 题解

递归比较直观，题目要求用迭代算法完成，所以用压栈的方法，从根节点开始，将所有左节点都压栈，到没有左节点为止，将栈顶出栈并输出，然后以栈顶的右节点为根节点再进行一次（如果没有右节点则再从栈顶取一个元素），直到遍历完所有节点。

## 标程

```python
from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution(object):
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        cur = root
        ret, stack = [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
        return ret


if __name__ == '__main__':
    print(
        Solution().inorderTraversal(
            TreeNode(1, None, TreeNode(2, TreeNode(3)))
        )
    )

```