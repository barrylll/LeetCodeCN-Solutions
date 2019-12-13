class Solution(object):
    def multiply(self, num1: str, num2: str) -> str:
        def single_mul(s, n):
            ret = ""
            up = 0
            s = s[::-1]
            for str_i in s:
                i = int(str_i)
                now = (i * n + up) % 10
                up = (i * n + up) // 10
                ret += str(now)
            if up > 0:
                ret += str(up)
            return ret[::-1]

        def two_sum(n1, n2):
            ret = ""
            if len(n2) >= len(n1):
                n2, n1 = n1, n2
            n1 = n1[::-1]
            n2 = n2[::-1]
            up = 0
            for i in range(len(n1)):
                if i < len(n2):
                    now = int(n1[i]) + int(n2[i]) + up
                    up = now // 10
                    now = now % 10
                    ret += str(now)
                else:
                    if up > 0:
                        now = int(n1[i]) + up
                        up = now // 10
                        now = now % 10
                        ret += str(now)
                    else:
                        ret += n1[i]
            if up > 0:
                ret = ret + str(up)
            return ret[::-1]

        if len(num2) >= len(num1):
            num2, num1 = num1, num2
        re = ""
        zeros = ""
        num2 = num2[::-1]
        for i in num2:
            re = two_sum(re, single_mul(num1, int(i)) + zeros)
            zeros += "0"
        if re[0] == "0" and len(re) > 1:
            re = "0"
        return re


if __name__ == '__main__':
    print(
        Solution().multiply("0", "43215")
    )
