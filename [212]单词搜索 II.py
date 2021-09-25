# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。 
# 
#  单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使
# 用。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f",
# "l","v"]], words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 12 
#  board[i][j] 是一个小写英文字母 
#  1 <= words.length <= 3 * 10⁴ 
#  1 <= words[i].length <= 10 
#  words[i] 由小写英文字母组成 
#  words 中的所有字符串互不相同 
#  
#  Related Topics 字典树 数组 字符串 回溯 矩阵 👍 556 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

df_x = [0, -1, 1, 0]
df_y = [-1, 0, 0, 1]
end_of_word = "#"
#Trie树、DFS、递归
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        if not words:
            return []
        self.result = set()

        #构建Trie树
        import collections
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char,collections.defaultdict())
            node[end_of_word] = end_of_word

        #遍历board中每个字母并依次检索其上、下、左、右的字母是否在Trie树中
        self.row_len = len(board)
        self.column_len = len(board[0])
        for row in range(self.row_len):
            for column in range(self.column_len):
                if board[row][column] in root:
                    self.dfs(board,row,column,"",root)
        return list(self.result)

    def dfs(self,board,row,column,cur_word,cur_dict):
        #递归终止条件
        cur_word += board[row][column]
        cur_dict = cur_dict[board[row][column]]
        #if board[row][column] == end_of_word:
        if end_of_word in cur_dict:
            #return self.result.add(cur_word)
            self.result.add(cur_word)

        #处理当前层
        # for i in range(4):
        #     x = row + df_x[i]
        #     y = column + df_y[i]
        # temp,board[row][column] = board[row][column],'*'
        temp,board[row][column] = board[row][column],'*'
        for i in range(4):
            x,y = row + df_x[i],column + df_y[i]
        # for row in range(self.row_len):
        #     for column in range(self.column_len):
        #         if 0 <= x < self.row_len and 0 <= y < self.column_len\
        #         and board[x][y] != '*' and board[x][y] in cur_dict:
        #             #下潜到下一层
        #             self.dfs(board,x,y,cur_word,cur_dict)
            if 0 <= x < self.row_len and 0 <= y < self.column_len\
            and board[x][y] != '*' and board[x][y] in cur_dict:
                self.dfs(board,x,y,cur_word,cur_dict)
        #恢复当前层
        board[row][column] = temp

obj = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
result = obj.findWords(board,words)
print(result)
# leetcode submit region end(Prohibit modification and deletion)
