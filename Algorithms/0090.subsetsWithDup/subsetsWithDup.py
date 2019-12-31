from typing import List


class Solution(object):
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(now):
            if now == -1:
                ret.append([])
                backtrack(now + 1)
            else:
                if now == len(nums):
                    return
                for i in ret[:]:
                    temp = i[:]
                    temp.append(nums[now])
                    temp.sort()
                    if temp not in ret:
                        ret.append(temp)
                backtrack(now + 1)

        ret = []
        backtrack(-1)
        return ret


if __name__ == '__main__':
    output = [4, 4, 4, 1, 4]
    print(
        Solution().subsetsWithDup(output)
    )
