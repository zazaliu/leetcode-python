class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        递推式，假设原先的字符串为"y231"，现在在它之前加一个数字得到"xy231"，如果x不为0，此时，如果"xy"不在1-26之间，
        那么原先能转换的种类不变，只是在每个字符串之前增加一个x转换后的字母；如果"xy"在1-26之间，那么除了在原先每个字
        符串之前增加x转换后的字母，还可能是在"231"转化之后的字符串前增加"xy"转化的字母。那如果x等于0呢，此时是一个非法
        字符串，让它默认为0。但不能跳出循环，因为在前面继续增加数字可能将字符串变为合法的。
        """
        lenth=len(s)
        if lenth == 0:
            return 0
        res=[0 for i in range(lenth+1)]
        res[lenth]=1
        res[lenth-1]=1 if s[lenth-1] != "0" else 0
        for i in range(lenth-2,-1,-1):
            if s[i] != "0":
                res[i]= res[i+1]+res[i+2] if int(s[i:i+2]) <= 26 else res[i+1]
        return res[0]