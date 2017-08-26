class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        从原字符串长度开始依次查找字符串的子字符串，判断子字符串是否为回文字符串，如果是，直接返回子字符串即可。
        （如果从单个字符依次查找子字符串，则需要遍历所有子字符串）
        """
        maxLenth=len(s)
        while maxLenth >= 0:
            for i in range(len(s)-maxLenth+1):
                subString=s[i:i+maxLenth]
                if subString == subString[::-1]:
                    return subString
            maxLenth=maxLenth-1
        return ''
