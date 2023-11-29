#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = []
        for i in range(0,len(nums)):
            temp.append(nums[i]*nums[i])
        
        temp.sort()
        return temp
        
# @lc code=end

