#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:    
       a = ""
       for i in digits:
          a += str(i)
       a = int(a)
       a += 1
       digits = []
       for i in str(a):
          digits.append(int(i))
       return digits
          

        

        
# @lc code=end

