class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        res=[]
        citations.sort()
        citations=citations[::-1]
        for i in range(len(citations)):
            if citations[i] >= i+1:
                res.append(i+1)
        return max(res) if len(res) > 0 else 0


s=Solution()
citations=[3,0,6,1,5]
print(s.hIndex(citations))