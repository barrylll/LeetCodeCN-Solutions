class Solution(object):
    def reverse(self, x: int) -> int:
        num = ""
        temp = abs(x)
        if temp == 0:
            return 0
        while temp != 0:
            n = temp % 10
            temp = temp // 10
            num = num + str(n)
        ret = int(num) if x >= 0 else -int(num)
        if ret > 2147483647 or ret < -2147483648:
            return 0
        else:
            return ret

if __name__ == '__main__':
    print(
        Solution().reverse(1463847412)
    )






