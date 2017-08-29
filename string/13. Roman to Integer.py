class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = 0
        temp = []
        for i in roman:
            temp.append(s.count(i))
        for j in range(13):
            if j%2 == 0 and j <= 10:
                res=res+integer[j]*(temp[j]-temp[j+1])
            else:
                res=res+integer[j]*temp[j]
        res=res-100*(temp[3]+temp[1])-10*(temp[5]+temp[7])-temp[9]-temp[11]
        return res