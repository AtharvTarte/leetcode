#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        intervals=sorted(intervals)
        a=intervals[0]
        l=[a]

        for i in range(len(intervals)):
            b=intervals[i]
            if b[0]<=a[1] and b[1]>a[1]:
                l[-1][1]=b[1]
            if b[0]>a[1]:
                l.append(b)
            a=l[-1]
        return l
# @lc code=end

