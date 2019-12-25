import collections


class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        dict_t = collections.Counter(t)
        left = right = 0
        temp = {}
        ans = (float("inf"), 0, 0)
        required = len(dict_t)
        in_window = 0
        while right < len(s):
            character = s[right]
            temp[character] = temp.get(character, 0) + 1
            if temp[character] == dict_t[character]:
                in_window += 1
            while left <= right and in_window == required:
                character = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                temp[character] -= 1
                if character in dict_t and temp[character] < dict_t[character]:
                    in_window -= 1
                left += 1
            right += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


if __name__ == '__main__':
    print(
        Solution().minWindow("ADOBECODEBANC", "ABC")
    )
