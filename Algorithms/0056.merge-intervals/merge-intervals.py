from typing import List


class Solution(object):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
        Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    )
