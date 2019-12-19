# 56. 合并区间

## 题意

给出一个区间的集合，请合并所有重叠的区间。

**示例1:**

```
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
```

**示例2:**

```
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
```

## 题解

判断是否重合只需要判断当前区间的左边界是否比目标区间的右边界小，如果是的话就需要合并。

## 标程
```python
from typing import List


class Solution(object):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        for i in intervals:
            if not ret or ret[-1][1] < i[0]:
                ret.append(i)
            else:
                ret[-1][1] = max(ret[-1][1], i[1])
        return ret


if __name__ == '__main__':
    print(
        Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    )

```