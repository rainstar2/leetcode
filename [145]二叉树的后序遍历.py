# 给定一个二叉树，返回它的 后序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [3,2,1] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 686 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    #递归
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            result.append(root.val)

        dfs(root)
        return result
# leetcode submit region end(Prohibit modification and deletion)
