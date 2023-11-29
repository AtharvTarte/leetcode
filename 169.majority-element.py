#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from statistics import mode
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return (mode(nums))


        
# @lc code=end

