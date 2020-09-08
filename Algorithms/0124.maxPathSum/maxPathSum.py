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
    def maxPathSum(self, root: TreeNode) -> int:
        global maxsum
        maxsum = float("-inf")

        def Rec(root: TreeNode):
            if root:
                left_val = max(Rec(root.left), 0)
                right_val = max(Rec(root.right), 0)

                temp = root.val + left_val + right_val

                global maxsum
                maxsum = max(maxsum, temp)

                return root.val + max(left_val, right_val)
            else:
                return 0

        Rec(root)
        return maxsum


if __name__ == '__main__':
    print(
        Solution().maxPathSum(
            TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        )
    )
