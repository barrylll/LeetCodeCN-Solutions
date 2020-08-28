from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = triangle[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
            dp[0] += triangle[i][0]
        ret = min(dp)
        return ret


if __name__ == '__main__':
    print(
        Solution().minimumTotal(
            [
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
            ]
        )
    )
