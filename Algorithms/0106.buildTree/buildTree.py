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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def backtrack(inord, postord, post_pos, left, right):
            if left > right:
                return None
            root = TreeNode(postord[post_pos])
            in_pos = 0
            for i in range(left, right + 1):
                if inord[i] == postord[post_pos]:
                    in_pos = i
                    break
            right_num = right - in_pos

            root.left = backtrack(inord, postord, post_pos - right_num - 1, left, in_pos - 1)
            root.right = backtrack(inord, postord, post_pos - 1, in_pos + 1, right)
            return root

        return backtrack(inorder, postorder, len(inorder) - 1, 0, len(inorder) - 1)


if __name__ == '__main__':
    print(
        Solution().buildTree(
            [9,3,15,20,7],
            [9,15,7,20,3]
        )
    )
