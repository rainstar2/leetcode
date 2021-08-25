# You are given an integer array nums. You are initially positioned at the array
# 's first index, and each element in the array represents your maximum jump lengt
# h at that position. 
# 
#  Return true if you can reach the last index, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jum
# p length is 0, which makes it impossible to reach the last index.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  0 <= nums[i] <= 105 
#  
#  Related Topics 贪心 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    #贪心算法
    def canJump(self, nums):
      max = 0
      for step,num in enumerate(nums):
        if max >= step and step + num > max:
          max = step + num
      return max >= step
# leetcode submit region end(Prohibit modification and deletion)
