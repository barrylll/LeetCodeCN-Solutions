# 99. 恢复二叉搜索树

## 题意

二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。。

**示例1:**
```
输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
```
**示例2:**
```
输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
```

**进阶:**  
使用 O(n) 空间复杂度的解法很容易实现。  
你能想出一个只使用常数空间的解决方案吗？

## 题解

如果没有常数空间的要求的话本题就是简单的中序遍历，找到不符合从小到大排列的两个数交换即可。

因为要求了常数空间，需要使用Morris遍历来进行中序遍历，题解参考了[sanjay-2](https://leetcode-cn.com/problems/recover-binary-search-tree/solution/python-morris-ji-chu-shang-tian-jia-ji-ju-luo-ji-b/)的题解，
在计算过程中利用了前序节点（中序遍历中本节点的前一个节点）的思想，同样是记录中序遍历中两个没有按照正常升序排列的节点的位置，将这两个节点的值进行交换。

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
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tmp = root
        first_node = None
        second_node = None
        flag = None

        while tmp:
            if tmp.left:
                pre = tmp.left
                while pre.right and pre.right != tmp:
                    pre = pre.right
                if not pre.right:
                    pre.right = tmp
                    tmp = tmp.left
                    continue
                pre.right = None
            if flag and flag.val > tmp.val:
                if first_node is None:
                    first_node = flag
                second_node = tmp
            flag = tmp
            tmp = tmp.right

        first_node.val, second_node.val = second_node.val, first_node.val


if __name__ == '__main__':
    print(
        Solution().recoverTree(
            TreeNode(1, TreeNode(3, None, TreeNode(2)))
        )
    )

```