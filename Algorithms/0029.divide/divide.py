class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        left = abs(dividend)
        right = abs(divisor)
        ret = count = 0
        while left >= right:
            right <<= 1
            count += 1
        while count > 0:
            count -= 1
            right >>= 1
            if left >= right:
                ret += 1 << count
                left -= right
        if (dividend > 0) ^ (divisor > 0):
            ret = -ret
        if ret > 2**31 - 1 or ret < -2**31:
            return 2**31 - 1
        else:
            return ret

if __name__ == '__main__':
    print(
        Solution().divide(-2147483648, 1)
    )
