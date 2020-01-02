from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution(object):
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        cur = root
        ret, stack = [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
        return ret


if __name__ == '__main__':
    print(
        Solution().inorderTraversal(
            TreeNode(1, None, TreeNode(2, TreeNode(3)))
        )
    )
