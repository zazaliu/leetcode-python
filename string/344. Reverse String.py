class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1=list(s)
        s1.reverse()
        return "".join(s1)
