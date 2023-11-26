#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left =0
        right = sum(nums)
        for index, nums in enumerate(nums):
            right-=nums
            if left==right:
                return index
            left+=nums           
        return -1
        
# @lc code=end

