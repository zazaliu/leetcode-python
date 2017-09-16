class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operator = []
        operatorNum = []
        s = s.replace(" ", "")
        lenth = len(s)
        start = 0
        for i in range(lenth):
            if s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/":
                operatorNum.append(int(s[start:i]))
                operator.append(s[i])
                start = i + 1
        operatorNum.append(int(s[start:]))
        for i in range(len(operator)):
            if operator[i] == "*":
                temp = operatorNum[i] * operatorNum[i + 1]
                operator[i] = "*"
                operatorNum[i] = temp
                operatorNum[i + 1] = 1
            if operator[i] == "/":
                temp = operatorNum[i] // operatorNum[i + 1]
                operator[i] = "*"
                operatorNum[i + 1] = temp
                operatorNum[i] = 1
        res = operatorNum[0]
        for i in range(len(operator)):
            if operator[i] == "*" and operatorNum[i] == 1:
                operator[i]="+"
                operatorNum[i]=0
        for i in range(len(operator)):
            if operator[i] == "+":
                res += operatorNum[i+1]
            if operator[i] == "-":
                res -= operatorNum[i + 1]
            if operator[i] == "*":
                res *= operatorNum[i+1]
        return str(operator)+str(operatorNum)
        # return res

s=Solution()
print(s.calculate(" 3+5 / 2 "))
print(s.calculate("2*3*4"))
print(s.calculate("12-3*4"))
print(s.calculate("1*2-3/4+5*6-7*8+9/10"))
print(s.calculate("14/3/2"))
print(s.calculate("1*1"))