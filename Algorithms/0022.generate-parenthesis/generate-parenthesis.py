from typing import List


class Solution(object):
    def generateParenthesis(self, n: int) -> List[str]:
        temp = set()

        def generater(generation="", left=0, right=0):
            if len(generation) == 2 * n:
                temp.add(generation)
            if left < n:
                generater(generation + "(", left + 1, right)
            if right < left:
                generater(generation + ")", left, right + 1)

        ret = []
        generater()
        for i in temp:
            ret.append(str(i))
        return ret


if __name__ == '__main__':
    print(
        Solution().generateParenthesis(4)
    )
