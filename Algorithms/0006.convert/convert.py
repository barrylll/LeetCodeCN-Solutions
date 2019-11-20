class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            ret = ""
            mod = 2 * (numRows - 1)
            for j in range(numRows):
                for i in range(len(s)):
                    if i % mod == j or i % mod == mod - j:
                        ret = ret + s[i]
            return ret

if __name__ == '__main__':
    print(
        Solution().convert("A", 1)
    )






