class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aList=a.split("+")
        bList=b.split("+")
        aR=int(aList[0])
        aI=int(aList[1][:len(aList[1])-1])
        bR=int(bList[0])
        bI=int(bList[1][:len(bList[1])-1])
        resR=aR*bR-aI*bI
        resI=aR*bI+aI*bR
        return str(resR)+"+"+str(resI)+"i"