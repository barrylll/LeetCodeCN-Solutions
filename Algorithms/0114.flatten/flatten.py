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
