# 105. 从前序与中序遍历序列构造二叉树

## 题意

根据一棵树的前序遍历与中序遍历构造二叉树。

**注意:**  
你可以假设树中没有重复的元素。

例如，给出
```
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
```
返回如下的二叉树：
```
    3
   / \
  9  20
    /  \
   15   7
```

## 题解

前序遍历的第一个节点是根节点，在中序遍历中找到这个节点，然后在他左边的都是左子树，右边的都是右子树，对左子树和右子树分别递归再找根节点、左子树、右子树。

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def backtrack(preord, inord, pre_pos, left, right):
            if left > right:
                return None
            root = TreeNode(preord[pre_pos])
            in_pos = 0
            for i in range(left, right + 1):
                if inord[i] == preord[pre_pos]:
                    in_pos = i
                    break
            left_num = in_pos - left

            root.left = backtrack(preord, inord, pre_pos + 1, left, in_pos - 1)
            root.right = backtrack(preord, inord, pre_pos + left_num + 1, in_pos + 1, right)
            return root

        return backtrack(preorder, inorder, 0, 0, len(inorder) - 1)


if __name__ == '__main__':
    print(
        Solution().buildTree(
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7]
        )
    )

```