# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [], l2 = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  两个链表的节点数目范围是 [0, 50] 
#  -100 <= Node.val <= 100 
#  l1 和 l2 均按 非递减顺序 排列 
#  
#  Related Topics 递归 链表 
#  👍 1850 👎 0


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    #递归
    def mergeTwoLists(self, l1:ListNode, l2:ListNode)->ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        l1:[1,2]
        l2:[1,3,4]
        """
        #递归终结条件：l1或l2均为空
        if not l1:
            return l2
        elif not l2:
            return l1
        #递归方法：l1的head和l2的head比较，谁的head小，谁就把自己的next和另一个链表作为参数继续调用函数
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists(l2.next,l1)
            return l2
# leetcode submit region
