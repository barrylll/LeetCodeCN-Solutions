from typing import List


class Solution(object):
    def grayCode(self, n: int) -> List[int]:
        def backtrack(num):
            if num == 0:
                return ["0"]
            if num == 1:
                return ["0", "1"]
            pre = backtrack(num - 1)
            ret = pre[:]
            for i in range(len(pre) - 1, -1, -1):
                temp = "1" + "0" * (num - 1 - len(pre[i])) + pre[i]
                ret.append(temp)
            return ret

        res = []
        for i in backtrack(n):
            res.append(int(i, 2))
        return res


if __name__ == '__main__':
    print(
        Solution().grayCode(4)
    )
