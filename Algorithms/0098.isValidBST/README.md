# 98. 验证二叉搜索树

## 题意

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

1.  节点的左子树只包含小于当前节点的数。
2.  节点的右子树只包含大于当前节点的数。
3.  所有左子树和右子树自身必须也是二叉搜索树。

**示例1:**
```
输入:
    2
   / \
  1   3
输出: true
```
**示例2:**
```
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
```
## 题解

递归。需要注意的是因为二叉搜索树的定义是“左子树的所有节点 < 根节点 < 右子树的所有节点”。所以在递归过程中需要始终维护两个值作为节点的左界和右界，
对于左子节点来说，右界为本节点的值，左界为本节点的左界，对于右子节点来说，左界为本节点的值，右界为本节点的右界。（可能有点绕，看代码就明白了）

## 标程

```python
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
    def isValidBST(self, root: TreeNode) -> bool:
        def check(node, left=float("-inf"), right=float("inf")):
            if not node:
                return True

            if node.val <= left or node.val >= right:
                return False

            if not check(node.right, node.val, right):
                return False
            if not check(node.left, left, node.val):
                return False
            return True

        return check(root)


if __name__ == '__main__':
    print(
        Solution().isValidBST(
            TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
        )
    )

```