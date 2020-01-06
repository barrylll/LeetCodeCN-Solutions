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
