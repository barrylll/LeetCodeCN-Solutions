# 124. 二叉树中的最大路径和

## 题意

给定一个**非空**二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径**至少包含一个节点**，且不一定经过根节点。

**示例1：**

```
输入：[1,2,3]

       1
      / \
     2   3

输出：6
```

**示例2：**

```
输入：[-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出：42
```

## 题解

递归。对每个节点计算这个节点能给上一个节点的最大贡献值，叶子节点的贡献值为节点本身的值，非叶子节点的贡献值为节点自身的值加上左右子节点贡献值的最大值如果贡献值为负数则置为`0`。
例如示例2中，15节点的贡献值是15，7节点的贡献值是7，20节点的贡献值是`20 + max(15, 7) = 35`。  
获得这个贡献值之后，对于每个节点，从这个节点经过的路径的最大值即为本节点的值加上左右节点的贡献值。对每个节点计算出经过该节点的路径的最大值，取其中最大的那个即可。


## 标程

```python
class TreeNode:
    def __init__(self, x, left=None, right=None, next = None):
        self.val = x
        self.left = left
        self.right = right
        self.next = next

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
    def maxPathSum(self, root: TreeNode) -> int:
        global maxsum
        maxsum = float("-inf")

        def Rec(root: TreeNode):
            if root:
                left_val = max(Rec(root.left), 0)
                right_val = max(Rec(root.right), 0)

                temp = root.val + left_val + right_val

                global maxsum
                maxsum = max(maxsum, temp)

                return root.val + max(left_val, right_val)
            else:
                return 0

        Rec(root)
        return maxsum


if __name__ == '__main__':
    print(
        Solution().maxPathSum(
            TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        )
    )

```