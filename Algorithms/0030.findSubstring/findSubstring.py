from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        if s == "" or words == []:
            return []
        one_size = len(words[0])
        all_size = len(words) * one_size
        words_map = dict()
        for i in words:
            if i not in words_map:
                words_map[i] = 1
            else:
                words_map[i] += 1
        for i in range(len(s) - all_size + 1):
            d = dict(words_map)
            if self.matchSubstring(s[i:i + all_size], d, one_size):
                ret.append(i)
        return ret

    def matchSubstring(self, s: str, d: dict, size: int):
        for i in range(0, len(s), size):
            key = s[i:i + size]
            if key in d:
                d[key] -= 1
                if d[key] == 0:
                    del d[key]
            else:
                return False
        if not d:
            return True


if __name__ == '__main__':
    print(
        Solution().findSubstring("aaaaa", ["a", "a", "a", "a", "a"])
    )
