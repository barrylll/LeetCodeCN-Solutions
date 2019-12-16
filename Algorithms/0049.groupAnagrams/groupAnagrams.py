from typing import List


class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        check = {}
        cnt = 0
        for i in strs:
            temp = list(i)
            temp.sort()
            if str(temp) not in check:
                to_be_append = [i]
                ret.append(to_be_append)
                check[str(temp)] = cnt
                cnt += 1
            else:
                temp = list(i)
                temp.sort()
                ret[check[str(temp)]].append(i)
        return ret


if __name__ == '__main__':
    print(
        Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    )
