class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=list(s.split())
        res.reverse()
        return " ".join(res)