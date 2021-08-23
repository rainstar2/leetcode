# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 
# 
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。” 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [2, 10⁵] 内。 
#  -10⁹ <= Node.val <= 10⁹ 
#  所有 Node.val 互不相同 。 
#  p != q 
#  p 和 q 均存在于给定的二叉树中。 
#  
#  Related Topics 树 深度优先搜索 二叉树 👍 1262 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #递归
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #recursion terminator
        if not root or root == p or root == q:
            return root

        #drill down
        #遍历左结点
        left = self.lowestCommonAncestor(root.left,p,q)
        #遍历右节点
        right = self.lowestCommonAncestor(root.right,p,q)
        #处理
        # 如果左右节点均为空，则root下均无p、q，返回空
        if not left and not right:
            return None
        # 如果有左节点，但右节点为空，则root左侧至少有pq其中一个或两者均有。而不管是哪种，left一定是最近祖先
        if not right:
            return left
        # 如果有右节点，但左结点为空，同上一个
        if not left:
            return right
        # 如果左右结点均有，则p、q在root的左右两侧，此时root为最近公共祖先
        return root
        
# leetcode submit region end(Prohibit modification and deletion)
