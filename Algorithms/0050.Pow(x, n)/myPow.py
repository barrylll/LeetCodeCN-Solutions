class Solution(object):
    def myPow(self, x: float, n: int) -> float:
        def backtrack(x, n):
            if n == 0:
                return 1
            elif n % 2 == 1:
                return x * (backtrack(x, n // 2) ** 2)
            else:
                return backtrack(x, n // 2) ** 2

        if n >= 0:
            return backtrack(x, n)
        else:
            return backtrack(1/x, -n)


if __name__ == '__main__':
    print(
        Solution().myPow(0.00001, 2147483647)
    )
