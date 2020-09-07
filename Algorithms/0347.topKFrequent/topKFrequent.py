from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        dic_sorted = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        ret = []
        for i in range(k):
            ret.append(dic_sorted[i][0])
        return ret


if __name__ == '__main__':
    print(
        Solution().topKFrequent(
            [1, 1, 1, 2, 2, 3], 2
        )
    )
