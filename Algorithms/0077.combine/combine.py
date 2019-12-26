from typing import List


class Solution(object):
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(now, num):
            if len(num) == k:
                ret.append(num[:])
            for i in range(now, n + 1):
                num.append(i)
                backtrack(i + 1, num)
                num.pop()

        ret = []
        backtrack(1, [])
        return ret


if __name__ == '__main__':
    print(
        Solution().combine(4, 2)
    )
