import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        res = [False,False]+[True for x in range(2, n)]
        i=2
        while i <= math.sqrt(n):
            if not res[i]:pass
            j=2
            while i*j < n:
                res[i*j]=False
                j+=1
            i+=1
        return res.count(True)


s=Solution()
n1=10
n2=100
print(s.countPrimes(n1))
print(s.countPrimes(n2))