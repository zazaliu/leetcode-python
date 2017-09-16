# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# For example:
# Given "25525511135",

# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

# 增加实例运行结果

# 解法：
# 递归，每次取字符串前面1到3位，并判断是否为合法值（0~255，非零值不能以0作为起始位），
# 剩余位继续重复以上过程，直至产生合法IP地址，并且原始字符串切割完毕。

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        self.strSplit(s,0,"",res)
        return res
    def strSplit(self,s,times,IP,res):
        if times == 4:
            if not s:
                res.append(IP[:-1])
            return
        for i in range(1,4):
            if i <= len(s):
                subIP=s[:i]
                if i == 1:
                    self.strSplit(s[i:],times+1,IP+subIP+".",res)
                if i == 2 and subIP[0] != "0":
                    self.strSplit(s[i:],times+1,IP+subIP+".",res)
                if i == 3 and subIP[0] != "0" and int(subIP) < 256:
                    self.strSplit(s[i:],times+1,IP+subIP+".",res)

s=Solution()
print(s.restoreIpAddresses("25525511135"))
