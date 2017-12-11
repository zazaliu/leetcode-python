class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numsDict = {}
        for i in nums:
            numsDict[i] = 1 if i not in numsDict else numsDict[i] + 1
        kList=[v for k,v in numsDict.items()]
        kList.sort()
        kList=kList[::-1]
        res=[]
        for i in range(k):
            for key,value in numsDict.items():
                if value == kList[i]:
                    res.append(key)
        return list(set(res))




s=Solution()
nums=[1,1,1,2,2,3]
k=2
nums1=[1,2]
k1=2
print(s.topKFrequent(nums1,k1))