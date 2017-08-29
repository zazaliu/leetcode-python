class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        先提取字符串的一半，然后乘以2，看生成串和原串是否相同，相同则true，否则提取字符串三分之一，
        然后乘以3，以此类推。
        """
        if not s or len(s) < 2:
            return False

        strlen = len(s)
        pos = strlen / 2
        while pos > 0:
            if strlen % pos == 0:
                substr = s[:pos]
                divisor = strlen / pos
                if substr*divisor == s:
                    return True
            pos -= 1
        return False
