# -*- coding: utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        ma = -1
        ret = ""
        # 初始化
        for i in range(0, len(s)):
            dp[i][i] = True
            if i < len(s) - 1:
                dp[i][i + 1] = (s[i] == s[i + 1])
        for j in range(0, len(s)):
            for i in range(0, j + 1):
                dp[i][j] = (s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]))
                if dp[i][j] and j - i > ma:
                    ma = j - i
                    ret = s[i: j + 1]
        return ret

    def manacher(self, s: str) -> str:
        s, origin_s = '#' + '#'.join(s) + '#', s
        
        n = len(s)
        RL = [0] * n
        pos, MaxRight = 0, 0
        axis = 0           # axis of the palindromic

        for i in range(n):
            if i < MaxRight:
                RL[i] = min(RL[2 * pos - i], MaxRight - i)
            else:
                RL[i] = 1
            
            # extend RL[i] while s[i - RL[i]: i + RL[i] + 1] is palindromic
            while i - RL[i] >= 0 and i + RL[i] < n and s[i - RL[i]] == s[i + RL[i]]:
                RL[i] += 1

            # update pos, MaxRight
            if i + RL[i] - 1 > MaxRight:
                pos, MaxRight = i, i + RL[i] - 1

            # update the ans
            if RL[axis] < RL[i]:
                axis = i

        origin_st, origin_len = (axis - (RL[axis] - 1)) // 2, RL[axis] - 1
        return origin_s[origin_st: origin_st + origin_len]


if __name__ == '__main__':
    print(
        Solution().longestPalindrome("dabab"),
        Solution().longestPalindrome("a"),
        Solution().longestPalindrome("")
    )
    print(Solution().manacher("cbbd"))
    print(Solution().manacher("dabab"))
    print(Solution().manacher("a"))
    print(Solution().manacher(""))
    