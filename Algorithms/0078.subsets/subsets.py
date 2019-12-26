from typing import List


class Solution(object):
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
                    ret.append(temp)
                backtrack(now + 1)

        ret = []
        backtrack(-1)
        return ret


if __name__ == '__main__':
    output = [i + 1 for i in range(10)]
    print(
        Solution().subsets(output)
    )
