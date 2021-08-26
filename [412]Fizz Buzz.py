# 写一个程序，输出从 1 到 n 数字的字符串表示。 
# 
#  1. 如果 n 是3的倍数，输出“Fizz”； 
# 
#  2. 如果 n 是5的倍数，输出“Buzz”； 
# 
#  3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。 
# 
#  示例： 
# 
#  n = 15,
# 
# 返回:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
#  
#  Related Topics 数学 字符串 模拟 👍 103 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    result = []
    #递归
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result.clear()
        self.recursion(1,n)
        return self.result

    def recursion(self,index,n):
        #设定终结条件
        if index > n:
            return

        if index % 3 == 0 and index % 5 == 0:
            self.result.append("FizzBuzz")

        elif index % 3 == 0:
            #终结前的处理
            self.result.append("Fizz")

        elif index % 5 == 0:
            self.result.append("Buzz")

        #处理当前递归层
        else:
            self.result.append(str(index))

        #下潜下层递归
        self.recursion(index + 1,n)

solution = Solution()
result = solution.fizzBuzz(15)
print(result)


# leetcode submit region end(Prohibit modification and deletion)
