class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 11:return num
        num1=num
        numList=[]
        while num > 0:
            numList.append(num%10)
            num=num//10
        numList=numList[::-1]
        for i in range(len(numList)-1):
            if numList[i] != max(numList[i:]):
                maxIndex,maxValue=i,numList[i]
                for j in range(i+1,len(numList)):
                    if numList[j] >= maxValue:
                        maxIndex,maxValue=j,numList[j]
                numList[i],numList[maxIndex]=numList[maxIndex],numList[i]
                numList=numList[::-1]
                res=0
                for k in range(len(numList)-1,-1,-1):
                    res=res*10+numList[k]
                return res
        return num1


num=1993
s=Solution()
print(s.maximumSwap(num))