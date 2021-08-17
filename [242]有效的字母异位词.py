# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "rat", t = "car"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, t.length <= 5 * 104 
#  s 和 t 仅包含小写字母 
#  
# 
#  
# 
#  进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
#  Related Topics 哈希表 字符串 排序 
#  👍 413 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    #哈希表（巧妙）
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        #定义一个长度为26的列表，用于统计每个字母的出现次数
        record = [0] * 26
        #遍历s，record中字母对应的位置+1
        for i in range(len(s)):
            #record中相对应的位置+1
            record[ord(s[i]) - ord('a')] += 1

        #遍历t，遇到s中出现的字母，在record中对应位置-1即可
        for i in range(len(t)):
            record[ord(t[i]) - ord('a')] -= 1

        """
        为什么record为0即代表两个字符大小相等，又代表所有字母的个数相等？
        举个例子（字符大小不等）。s = abc和t = abcd。record中对s的a、b、c均+1；再遍历
        t，所有a、b、c的均-1，d+1，这样下来record还是有值的，说明两个字符串
        不相等。
        再举个例子（字符大小相等但字母个数不相等）。s = abc和t = aab。record对s的a、b、c
        均+1，遍历t时a的位置为-1，b的位置为0，c的位置为1，这样record依然还是有值的，说明
        两个字符串所有字母个数不等
        当遍历A字符串的字母统计了4个，遍历B字符串时为0，则说明字母个数相等；当record为0，即每个
        字母的位置都为0，则表示两个字符串大小相等
        """
        #如果record中所有的下标没有元素对应，即record为空列表，则返回true
        for i in range(26):
            if record[i] != 0:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
# leetcode submit region end(Prohibit modification and deletion)
