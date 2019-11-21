class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            div = 1
            while x // div >= 10:
                div = div * 10
            while x > 0:
                left = x // div
                right = x % 10
                if left != right:
                    return False
                else:
                    x = x % div
                    x = x // 10
                    div = div // 100
            return True

if __name__ == '__main__':
    print(
        Solution().isPalindrome(1001)
    )
