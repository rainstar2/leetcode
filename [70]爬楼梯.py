# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 记忆化搜索 数学 动态规划 
#  👍 1806 👎 0


class Solution(object):
    #mine
    #递归
    # def climbStairs(self, n):
    #     if n == 0 or n == 1:
    #         return 1
    #     else:
    #         return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    #哈希表
    def climbStairs(self, n):
        list = dict()
        list[0] = 1
        list[1] = 1
        for i in range(2,n + 1):
            list[i] = list[i - 1] + list[i - 2]
        return list[n]
# leetcode submit region end(Prohibit modification and deletion)
