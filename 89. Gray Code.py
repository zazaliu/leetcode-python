class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:return [0]
        res=[[0],[1]]
        for i in range(1,n):
            left,right=[],[]
            for j in res:
                left.append([0]+j)
                right.append([1]+j)
            right=right[::-1]
            res=left+right
        return self.list2int(res)
    def list2int(self,res):
        greyRes=[]
        for i in res:
            greySum=0
            length=len(i)
            for j in range(length):
                if i[j] == 1:greySum+=2**(length-1)
                length-=1
            greyRes.append(greySum)
        return greyRes




s=Solution()
n1=2
n2=3
print(s.grayCode(n1))
print(s.grayCode(n2))