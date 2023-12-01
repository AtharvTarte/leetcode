#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []
        l = len(nums)
        for i in range(0,len(nums) - 1):
            a = i + 1
            while a < l:
                if nums[i] == nums[a]:
                    temp.append(nums[a])
                    nums.remove(nums[a])
                    l -= 1
                else:
                    a += 1                   

           
        nums = nums + temp
        k = len(nums) - len(temp)
        return k


        
# @lc code=end

