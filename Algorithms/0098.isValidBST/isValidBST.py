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
