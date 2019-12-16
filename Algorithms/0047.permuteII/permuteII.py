from typing import List


class Solution(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        from copy import deepcopy
        ret = []

        def backtrack(now, num):
            if not num:
                if len(now) > 0 and now not in ret:
                    ret.append(now)
            else:
                for i in range(len(num)):
                    if i > 0 and num[i] == num[i - 1]:
                        continue
                    nxt_num = deepcopy(num)
                    nxt_num.pop(i)
                    nxt_now = deepcopy(now)
                    nxt_now.append(num[i])
                    backtrack(nxt_now, nxt_num)

        nums.sort()
        backtrack([], nums)
        return ret


if __name__ == '__main__':
    print(
        Solution().permute([1,1,3,2])
    )
