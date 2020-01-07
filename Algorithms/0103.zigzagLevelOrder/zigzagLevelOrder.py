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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def backtrack(queue):
            nxt_queue, temp = [], []
            while queue:
                cur = queue.pop(0)
                temp.append(cur.val)
                if cur.left:
                    nxt_queue.append(cur.left)
                if cur.right:
                    nxt_queue.append(cur.right)
            if temp:
                ret.append(temp)
                backtrack(nxt_queue)

        if not root:
            return []
        ret = []
        backtrack([root])
        for i in range(len(ret)):
            if i % 2 == 1:
                ret[i] = ret[i][::-1]
        return ret


if __name__ == '__main__':
    print(
        Solution().zigzagLevelOrder(
            TreeNode(2, TreeNode(1), TreeNode(3))
        )
    )
