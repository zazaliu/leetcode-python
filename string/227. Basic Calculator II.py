class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        思路：将字符串处理为两个list，一个操作数列表，一个操作符列表，然后遍历操作符列表，
        初始化一个list作为堆栈，根据运算优先级，做以下运算：
            “+”：不做处理，直接将操作数放入堆栈；
            “-”：将下一个操作数取相反数放入堆栈；
            “*”：取栈顶元素与下一个操作数做乘法，将结果放入堆栈；
            “/”：取栈顶元素与下一个操作数做除法，将结果放入堆栈（注意，若栈顶元素为负值，应先转变为整数做除法，对结果取相反数）；
        最后将堆栈元素求和即为结果
        """
        operator = []               # 操作符
        operatorNum = []            # 操作数
        s = s.replace(" ", "")
        lenth = len(s)
        start = 0
        for i in range(lenth):
            if s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/":
                operatorNum.append(int(s[start:i]))
                operator.append(s[i])
                start = i + 1
        operatorNum.append(int(s[start:]))
        res = [operatorNum[0]]
        for i in range(len(operator)):
            if operator[i] == "*":
                temp = res.pop() * operatorNum[i + 1]
            if operator[i] == "/":
                j = res.pop()
                if j < 0:
                    temp = -(abs(j) // operatorNum[i + 1])
                else:
                    temp = j // operatorNum[i + 1]
            if operator[i] == "-":
                temp = -operatorNum[i + 1]
            if operator[i] == "+":
                temp = operatorNum[i + 1]
            res.append(temp)
        return sum(res)


s=Solution()
print(s.calculate(" 3+5 / 2 "))
print(s.calculate("2*3*4"))
print(s.calculate("12-3*4"))
print(s.calculate("1*2-3/4+5*6-7*8+9/10"))
print(s.calculate("14/3/2"))
print(s.calculate("1*1"))