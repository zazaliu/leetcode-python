class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(nums,[],res)
        return res
    def dfs(self,nums,nth,res):
        if not nums:
            res.append(nth)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],nth+[nums[i]],res)