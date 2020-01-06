class Solution(object):
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        tree_num = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                tree_num[i][j] = dp[j - 1] * dp[i - j]
                dp[i] += tree_num[i][j]
        return dp[n]


if __name__ == '__main__':
    print(
        Solution().numTrees(5)
    )
