#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        a = 0
        for i in nums:
            a += i
            ans.append(a)
        return ans
# @lc code=end

