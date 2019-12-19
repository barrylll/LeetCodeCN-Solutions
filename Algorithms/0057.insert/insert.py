from typing import List


class Solution(object):
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ret = []
        for i in intervals:
            if not ret or ret[-1][1] < i[0]:
                ret.append(i)
            else:
                ret[-1][1] = max(ret[-1][1], i[1])
        return ret


if __name__ == '__main__':
    print(
        Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    )
