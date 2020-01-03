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
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        from copy import deepcopy

        def generator(nums):
            if not nums:
                return [None]
            trees = []
            for i in range(len(nums)):
                root = TreeNode(nums[i])
                left_trees = generator(nums[:i])
                right_trees = generator(nums[i + 1:])
                for l in left_trees:
                    for r in right_trees:
                        root.left = l
                        root.right = r
                        trees.append(deepcopy(root))
            return trees

        num = [i + 1 for i in range(n)]
        ret = generator(num)
        return ret


if __name__ == '__main__':
    print(
        Solution().generateTrees(0)
    )
