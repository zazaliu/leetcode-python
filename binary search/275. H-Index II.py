class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations=citations[::-1]
        if len(citations) < 1:return 0
        left,right=0,len(citations)-1
        while left < right:
            mid=left+(right-left)//2
            if citations[mid] >= mid+1:left=mid
            else:right=mid-1
            if left+1 == right:
                if citations[right] >= right+1:
                    return right+1
                else:break
        return 0 if left == 0 and citations[0] ==0 else left+1



s=Solution()
citations=[0,1]
print(s.hIndex(citations))