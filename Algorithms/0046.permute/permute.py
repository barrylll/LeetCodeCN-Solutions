from typing import List


class Solution(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        from copy import deepcopy
        ret = []

        def backtrack(now, num):
            if not num:
                if len(now) > 0:
                    ret.append(now)
            else:
                for i in num:
                    nxt_num = deepcopy(num)
                    nxt_num.remove(i)
                    nxt_now = deepcopy(now)
                    nxt_now.append(i)
                    backtrack(nxt_now, nxt_num)

        backtrack([], nums)
        return ret


if __name__ == '__main__':
    print(
        Solution().permute([111, 222, 3333, 666])
    )
