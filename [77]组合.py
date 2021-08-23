# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 
# 
#  你可以按 任何顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, k = 1
# 输出：[[1]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
#  Related Topics 数组 回溯 👍 671 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    num_list = []
    result_list = []
    #递归 - 回溯
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        self.result_list = []
        self.recursion(n,k,1)
        return self.result_list

    def recursion(self,n,k,start_index):
        # 递归终结条件
        if len(self.num_list) == k:
            # 处理返回结果
            #print(self.num_list)
           #print(self.result_list)
            self.result_list.append(self.num_list[:])
            return


        # 处理当前层逻辑
        for i in range(start_index,n + 1):
            self.num_list.append(i)
            # 下探到下一层
            self.recursion(n,k,i + 1)
            # 清理当前层
            self.num_list.pop()
        #return
