class Solution(object):
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        max_sub_len = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ")" and s[i - 1] == "(":
                max_sub_len[i] = max_sub_len[i - 2] + 2
            elif s[i] == ")" and s[i - 1] == ")":
                if i - max_sub_len[i - 1] > 0 and s[i - max_sub_len[i - 1] - 1] == "(":
                    max_sub_len[i] = max_sub_len[i - 1] + ((max_sub_len[i - max_sub_len[i - 1] - 2]
                                                            if i - max_sub_len[i - 1] >= 2 else 0) + 2)
        return max(max_sub_len)


if __name__ == '__main__':
    print(
        Solution().longestValidParentheses("()()()(((()")
    )
