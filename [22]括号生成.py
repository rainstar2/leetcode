# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  有效括号组合需满足：左括号必须以正确的顺序闭合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics 字符串 动态规划 回溯 👍 1978 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    #递归
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        str = ""
        result_list = []
        result = self.recursion(0, 0, n, str,result_list)
        result_list.append(result)
        result_list = list(filter(None,result_list))
        return result_list

    def recursion(self,left, right, n, str,list):
        # 递归终结条件
        if left == n and right == n:
            # 处理返回结果
            #print(str)
            list.append(str)
            return

        # 处理当前层逻辑
        if left < n:
            self.recursion(left + 1, right, n, str + "(",list)
        if left > right:
            self.recursion(left, right + 1, n, str + ")",list)

        # 下探到下一层

        # 清理当前层(self,level,max):
# leetcode submit region end(Prohibit modification and deletion)
