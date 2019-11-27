from typing import List


class Solution(object):
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
               "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        ret = []

        def combine(combination, digits_):
            if digits_ == "":
                if len(combination) > 0:
                    ret.append(combination)
            else:
                for i in dic[digits_[0]]:
                    combine(combination + i, digits_[1:])

        combine("", digits)
        return ret

if __name__ == '__main__':
    print(
        Solution().letterCombinations("23")
    )
