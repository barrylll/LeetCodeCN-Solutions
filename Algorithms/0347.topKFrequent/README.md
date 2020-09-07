# 347. 前 K 个高频元素

## 题意

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

**示例1：**

```
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```

**示例2：**

```
输入: nums = [1], k = 1
输出: [1]
```

**提示：**
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。  
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。  
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。  
你可以按任意顺序返回答案。  

## 题解

遍历一遍`nums`，将`nums`中所有的元素以及其对应的出现频率组成一个`dict`，
对`dict`按照`value`从高到低排序，取前`k`位即可。

## 标程

```python
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

```