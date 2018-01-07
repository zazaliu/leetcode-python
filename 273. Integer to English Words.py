class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        num1=[1000000000,1000000,1000]
        s=[' Billion',' Million',' Thousand','']
        num2=[]
        res=''
        for i in range(3):
            quotient=num//num1[i]
            num2.append(quotient)
            num-=quotient*num1[i]
        num2.append(num)
        for i in range(len(num2)):
            if num2[i] != 0:
                res=res+self.numberToString(num2[i])+s[i]
        return res.lstrip() if res != "" else "Zero"
    def numberToString(self,num):
        strList1=[""," One"," Two"," Three"," Four"," Five"," Six"," Seven"," Eight"," Nine"," Ten",
                  " Eleven"," Twelve"," Thirteen"," Fourteen"," Fifteen"," Sixteen"," Seventeen",
                  " Eighteen"," Nineteen"," Twenty"]
        strList2=['','',' Twenty',' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        res=''
        if num >= 100:
            hundred=num//100
            res=res+strList1[hundred]+" Hundred"
            num=num-hundred*100
        if num > 20:
            ten=num//10
            res=res+strList2[ten]
            num=num-ten*10
        res=res+strList1[num]
        return res





s=Solution()
num1=2147483612
num=5643
print(s.numberToWords(num1))