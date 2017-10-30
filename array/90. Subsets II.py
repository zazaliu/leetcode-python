class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                temp = res[j] + [nums[i]]
                # res.append(temp)
                if temp not in res:
                    res.append(temp)
        return res

s=Solution()
print(s.subsetsWithDup([4,4,4,1,4]))