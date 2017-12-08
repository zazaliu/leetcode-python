class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res=[]
        while n != 1:
            temp=[]
            while n > 0:
                temp.append(n%10)
                n=n//10
            temp.sort()
            if temp in res:
                return False
            else: res.append(temp)
            n=0
            for i in temp:
                n+=i*i
        return True



s=Solution()
n1=19
n2=11
print(s.isHappy(n1))
print(s.isHappy(n2))