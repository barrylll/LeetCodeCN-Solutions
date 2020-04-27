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
