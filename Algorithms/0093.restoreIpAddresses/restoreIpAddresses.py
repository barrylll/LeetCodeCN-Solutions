from typing import List


class Solution(object):
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(now_s):
            return int(now_s) <= 255 if now_s[0] != "0" else len(now_s) == 1

        def update_output(curr_pos):
            segment = s[curr_pos + 1:len(s)]
            if check(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos=-1, dots=3):
            for i in range(prev_pos + 1, min(len(s) - 1, prev_pos + 4)):
                now_s = s[prev_pos + 1:i + 1]
                if check(now_s):
                    segments.append(now_s)
                    if dots - 1 == 0:
                        update_output(i)
                    else:
                        backtrack(i, dots - 1)
                    segments.pop()

        output, segments = [], []
        backtrack()
        return output


if __name__ == '__main__':
    print(
        Solution().restoreIpAddresses(
            "25525511135"
        )
    )
