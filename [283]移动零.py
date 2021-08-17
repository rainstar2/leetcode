# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 1175 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    #双指针
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        if not nums:
            return 0

        #定义一个变量j，作为存放非0数据的列表下标
        j = 0
        for i in range(len(nums)):
            #如果遍历到非0的数字，直接交给nums[j]存放。这样遍历完整个列表，j的位置是在最后一个非0数字上的
            if nums[i]:
                nums[j] = nums[i]
                j += 1

        #既然j的位置是在最后一个非0的数字上，则j后面的数字可以全部重置为0
        for i in range(j,len(nums)):
            nums[i] = 0

        return nums
# leetcode submit region end(Prohibit modification and deletion)
