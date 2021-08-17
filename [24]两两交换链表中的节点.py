# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 100] 内 
#  0 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。） 
#  Related Topics 递归 链表 
#  👍 1008 👎 0


class Solution(object):
    #递归
    def swapPairs(self, head:ListNode)-> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #如果链表没有结点，或者只有一个结点，返回链表
        if not head or not head.next:
            return head

        #定义新链表，它的头结点等于原链表的第二个结点
        newhead = head.next
        #第二个结点赋值给新的头结点后就空了，所以把新链表的第二个结点赋值给原链表的第二个结点
        head.next = self.swapPairs(newhead.next)
        #此时新链表的第二个结点空了，然后把原链表的头结点赋值给新链表的第二个结点
        newhead.next = head
        #返回新链表
        return newhead
# leetcode submit region end(Prohibit modification and deletion)
