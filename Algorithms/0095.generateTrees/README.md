# 95. 不同的二叉搜索树 II

## 题意

给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

**示例:**
```
输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```
## 题解

递归。将`i`遍历一遍`1~n`，将所有小于`i`的数放到`i`的左子树，将所有大于`i`的数放到`i`的右子树，递归的返回值是所有的子树集合。

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
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        from copy import deepcopy

        def generator(nums):
            if not nums:
                return [None]
            trees = []
            for i in range(len(nums)):
                root = TreeNode(nums[i])
                left_trees = generator(nums[:i])
                right_trees = generator(nums[i + 1:])
                for l in left_trees:
                    for r in right_trees:
                        root.left = l
                        root.right = r
                        trees.append(deepcopy(root))
            return trees

        num = [i + 1 for i in range(n)]
        ret = generator(num)
        return ret


if __name__ == '__main__':
    print(
        Solution().generateTrees(3)
    )

```