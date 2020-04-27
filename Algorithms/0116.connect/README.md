# 116. 填充每个节点的下一个右侧节点指针

## 题意

给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

**示例：**

![<116_sample>](<https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/116_sample.png>)

```
输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
```

## 题解

一层一层从左到右遍历一遍整棵树，对于每一个节点，它的左节点的`next`指向它的右节点，它的右节点的`next`指向它的`next`节点（如果存在）的左节点。  
代码表示为：`cur.left.next = cur.right，cur.right.next = cur.next.left`  

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
    def connect(self, root: 'TreeNode') -> 'TreeNode':
        first = cur = root
        if not cur:
            return cur
        cur.next = None
        queue = []
        while cur or queue:
            if cur.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                else:
                    cur.right.next = None
            if cur and (cur.left is not None or cur.right is not None):
                queue.append(cur.left)
                queue.append(cur.right)
            cur = queue.pop(0) if queue else None
        return first


if __name__ == '__main__':
    print(
        Solution().connect(
            TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        )
    )

```