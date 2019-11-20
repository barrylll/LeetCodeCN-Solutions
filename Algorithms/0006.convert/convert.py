class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            ret = ["" for _ in range(numRows)]
            mod = 2 * (numRows - 1)
            for i in range(len(s)):
                t = i % mod
                if t < numRows:
                    ret[t] = ret[t] + s[i]
                else:
                    ret[mod - t] = ret[mod - t] + s[i]
            return "".join(ret)

if __name__ == '__main__':
    print(
        Solution().convert("LEETCODEISHIRING", 3)
    )






