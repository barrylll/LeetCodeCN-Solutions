# 114. 二叉树展开为链表

## 题意

给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

```
    1
   / \
  2   5
 / \   \
3   4   6
```
将其展开为：
```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

## 题解

根据示例可以看出题目要求是将二叉树展开为前序遍历的链表，那么即能够保证**根节点->左子树->右子树**的顺序遍历，在每次遍历的时候将右子树插到左子树的最右侧，将左子树接到根节点的右边即可。

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
    def flatten(self, root: TreeNode) -> None:
        while root:
            if root.left is None:
                root = root.right
            else:
                temp = root.left
                while temp.right:
                    temp = temp.right
                temp.right = root.right
                root.right = root.left
                root.left = None
                root = root.right


if __name__ == '__main__':
    print(
        Solution().flatten(
            TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
        )
    )

```