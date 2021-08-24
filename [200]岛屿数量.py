# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '
# 0's (water), return the number of islands. 
# 
#  An island is surrounded by water and is formed by connecting adjacent lands h
# orizontally or vertically. You may assume all four edges of the grid are all sur
# rounded by water. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] is '0' or '1'. 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(grid,i,j):
            # 递归终结条件
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
                # 处理返回结果
                return
            # 处理当前层逻辑
            grid[i][j] = '0'

            # 下探到下一层
            dfs(grid,i + 1,j)
            dfs(grid,i - 1,j)
            dfs(grid,i,j + 1)
            dfs(grid,i,j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid,i,j)
                    count += 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
