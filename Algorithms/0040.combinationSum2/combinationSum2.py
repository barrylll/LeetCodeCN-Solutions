from typing import List

class Solution(object):
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from copy import deepcopy
        candidates.sort()

        def backtrack(tar, s=candidates):
            if tar == 0:
                return [[]]
            re = []
            for i in range(len(s)):
                if s[i] <= tar:
                    if i > 0 and s[i] == s[i - 1]:
                        continue
                    s_temp = deepcopy(s)
                    s_temp.pop(i)
                    for j in backtrack(tar - s[i], s_temp):
                        j.append(s[i])
                        re.append(j)
                else:
                    break
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
        Solution().combinationSum2([1,1,1,3,4], 7)
    )
