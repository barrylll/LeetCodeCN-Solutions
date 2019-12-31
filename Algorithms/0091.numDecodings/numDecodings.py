class Solution(object):
    def numDecodings(self, s: str) -> int:
        dp = [1 for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1]
            if i == 1:
                dp[i] = 1 if 1 <= int(s[i - 1]) <= 9 else 0
            if i > 1 and 1 <= int(s[i - 1]) <= 6 and 1 <= int(s[i - 2]) <= 2:
                dp[i] += dp[i - 2]
            if i > 1 and int(s[i - 1]) == 0:
                if 1 <= int(s[i - 2]) <= 2:
                    dp[i] = dp[i - 2]
                else:
                    return 0
            if i > 1 and 7 <= int(s[i - 1]) <= 9 and int(s[i - 2]) == 1:
                dp[i] += dp[i - 2]
        return dp[len(s)]


if __name__ == '__main__':
    print(
        Solution().numDecodings("110")
    )
