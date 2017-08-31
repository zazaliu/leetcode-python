class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=len(s)
        if len(s) == 0 or len(s) == 1:
            return res
        for i in range(2,len(s)):
            for j in range(len(s)-i+1):
                substring=s[j:j+i]
                if substring == substring[::-1]:
                    res+=1
        return res+1 if s == s[::-1] else res