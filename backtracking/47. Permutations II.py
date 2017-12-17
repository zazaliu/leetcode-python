class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(nums,[],res)
        return res
    def dfs(self,nums,nth,res):
        if not nums:
            if nth not in res:
                res.append(nth)
            else:return
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],nth+[nums[i]],res)