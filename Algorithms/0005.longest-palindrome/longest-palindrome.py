# -*- coding: utf-8 -*-
class Solution:
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
                    ret = s[i:j + 1]
        return ret



if __name__ == '__main__':
    print(
        Solution().longestPalindrome("dabab"),
        Solution().longestPalindrome("a"),
        Solution().longestPalindrome("")
    )






