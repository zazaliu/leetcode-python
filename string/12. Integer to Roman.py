class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        """
        用词典存储整数到罗马数字结果有错，不晓得原因
        """
        res = ""
        integer=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        for i in range(13):
            while num >= integer[i]:
                res = res+roman[i]
                num = num-integer[i]
        return res