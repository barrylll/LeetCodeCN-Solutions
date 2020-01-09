# 109. 有序链表转换二叉搜索树

## 题意

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

**示例:**
```
给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
```

## 题解

把链表存到一个`list`中，每次取中位数作为根节点，左边的`list`递归构建左树，右边的`list`递归构建右树。

## 标程

```python
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        ret = []
        cur = self
        while cur is not None:
            ret.append(cur.val)
            cur = cur.next
        return str(ret)


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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def buildTree(tree_list):
            if not tree_list:
                return None
            mid = (len(tree_list) - 1) // 2
            root = TreeNode(tree_list[mid])
            root.left = buildTree(tree_list[:mid])
            root.right = buildTree((tree_list[mid + 1:]))
            return root

        lst = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next
        tree_root = buildTree(lst)
        return tree_root


if __name__ == '__main__':
    print(
        Solution().sortedListToBST(
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
        )
    )

```