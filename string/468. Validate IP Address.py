class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if IP.count(".") == 3:
            IPList=IP.split(".")
            for i in IPList:
                if not i.isnumeric():
                    return "Neither"
                if int(i)<0 or int(i)>255:
                    return "Neither"
                elif len(i)>1 and i[0]=="0":
                    return "Neither"
            return "IPv4"
        elif IP.count(":") == 7:
            IPList=IP.split(":")
            for i in IPList:
                hexList=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
                for j in i:
                    if j.lower() not in hexList:
                        return "Neither"
                if i=="":
                    return "Neither"
                iNum=int(i,16)
                if iNum<0 or iNum>65535:
                    return "Neither"
                elif len(i)>4 and i[0]=="0":
                    return "Neither"
            return "IPv6"
        return "Neither"