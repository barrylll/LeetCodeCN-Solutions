# -*- coding: utf-8 -*-

class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(30)] for _ in range(30)]
        dp[-1][-1] = True

        # 预处理，p 头部的 * 可以跟空串匹配
        for i in range(len(p)):
            if p[i] == '*' and dp[-1][i - 2]:
                dp[-1][i] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i][j - 2]
                    elif p[j - 1] != s[i]:
                        dp[i][j] = dp[i][j - 2]

        return dp[len(s) - 1][len(p) - 1]

if __name__ == '__main__':
    print(
        Solution().isMatch("aab", "c*a*b")
    )
