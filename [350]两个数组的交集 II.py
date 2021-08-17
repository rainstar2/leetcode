# 给定两个数组，编写一个函数来计算它们的交集。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
#  
# 
#  示例 2: 
# 
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9] 
# 
#  
# 
#  说明： 
# 
#  
#  输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。 
#  我们可以不考虑输出结果的顺序。 
#  
# 
#  进阶： 
# 
#  
#  如果给定的数组已经排好序呢？你将如何优化你的算法？ 
#  如果 nums1 的大小比 nums2 小很多，哪种方法更优？ 
#  如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？ 
#  
#  Related Topics 数组 哈希表 双指针 二分查找 排序 
#  👍 536 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    #双指针
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        """
        1.排序
        2.双指针遍历两个列表，出现相同的记录下来，否则指针下标累加
        """
        nums1.sort()
        nums2.sort()
        result,left,right = [],0,0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                result.append(nums1[left])
                left += 1
                right += 1
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
