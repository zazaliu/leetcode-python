class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit=int(digits[0])
        for i in range(1,len(digits)):
            digit=digit*10+int(digits[i])
        digit=digit+1
        res=[]
        while digit > 0:
            res.append(digit%10)
            digit/=10
        res.reverse()
        return res