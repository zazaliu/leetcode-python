class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hLenth=len(haystack)
        nLenth=len(needle)
        for i in range(hLenth-nLenth+1):
            for j in range(nLenth):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i
        return -1
