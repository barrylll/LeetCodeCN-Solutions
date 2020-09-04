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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def Rec(root, path):
            if root:
                path += str(root.val)
                if root.left is None and root.right is None:
                    ret.append(path)
                else:
                    path += "->"
                    Rec(root.left, path)
                    Rec(root.right, path)

        ret = []
        Rec(root, "")
        return ret


if __name__ == '__main__':
    print(
        Solution().binaryTreePaths(
            TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
        )
    )
