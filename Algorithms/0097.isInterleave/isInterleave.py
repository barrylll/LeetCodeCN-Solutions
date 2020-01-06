class Solution(object):
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == j == 0:
                    dp[i][j] = True
                else:
                    if (j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) \
                            or (i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]):
                        dp[i][j] = True
        return dp[len(s1)][len(s2)]


if __name__ == '__main__':
    print(
        Solution().isInterleave("a", "", "a")
    )
