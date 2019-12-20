class Solution(object):
    def getPermutation(self, n: int, k: int) -> str:
        def cal_factorial(n):
            now = 1
            for i in range(n):
                now = now * (i + 1)
                factorial_num.append(now)

        def num_list(n):
            nums = []
            for i in range(n):
                nums.append(i + 1)
            return nums

        def backtrack(n, k, nums):
            div = factorial_num[n - 1]
            next_k = k % div
            group = k // div + (1 if next_k > 0 else 0) - 1
            temp = nums[group]
            nums.pop(group)
            if n - 1 > 0:
                return str(temp) + backtrack(n - 1, next_k, nums)
            else:
                return str(temp)

        factorial_num = [1]
        cal_factorial(n)
        return backtrack(n, k, num_list(n))


if __name__ == '__main__':
    print(
        Solution().getPermutation(3, 3)
    )
