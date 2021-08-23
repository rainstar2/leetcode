# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
# 
#  假设一个二叉搜索树具有如下特征： 
# 
#  
#  节点的左子树只包含小于当前节点的数。 
#  节点的右子树只包含大于当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  示例 1: 
# 
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#  
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 1179 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recursion(root,None,None)
    #递归
    def recursion(self,node,lower,upper):
        # 递归终结条件
        if not node:
            # 处理返回结果
            return True

        # 处理当前层逻辑
        val = node.val
        if lower != None and val <= lower:
            return False
        if upper != None and val >= upper:
            return False

        # 下探到下一层
        if not self.recursion(node.left,lower,val):
            return False
        if not self.recursion(node.right,val,upper):
            return False

        return True

        # 清理当前层
# leetcode submit region end(Prohibit modification and deletion)
# leetcode submit region end(Prohibit modification and deletion)
