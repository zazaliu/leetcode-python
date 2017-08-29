class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        """
        int("100",2) // 其他进制转换为二进制数，第一个参数加引号，因为二进制数为字符串，第二个参数为当前数的进制数
        bin(100) // 十进制数转换为二进制数，默认当前数为十进制
        oct(100) // 十进制数转换为八进制数，默认当前数为十进制
        hex(100) // 十进制数转换为十六进制数，默认当前数为十进制
        """
        return bin(int(a,2)+int(b,2))[2::]