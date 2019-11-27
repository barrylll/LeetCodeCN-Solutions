class Solution(object): 
    def intToRoman(self, num: int) -> str:
        nu = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ch = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        temp = num
        ret = ""
        while temp > 0:
            for i in range(len(ch)):
                while temp - nu[i] >= 0:
                    ret += ch[i]
                    temp -= nu[i]
        return ret

if __name__ == '__main__':
    print(
        Solution().intToRoman(1994)
    )
