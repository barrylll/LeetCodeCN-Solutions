from typing import List


class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(tar):
            if tar == 0:
                return [[]]
            re = []
            for i in candidates:
                if i <= tar:
                    for j in backtrack(tar - i):
                        j.append(i)
                        re.append(j)
            return re

        temp = backtrack(target)
        ret = []
        for i in temp:
            i.sort()
            if i and i not in ret:
                ret.append(i)
        return ret


if __name__ == '__main__':
    print(
        Solution().combinationSum([1, 2, 3, 4, 5], 6)
    )
