class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        动态规划，遍历整个list,保存子序列积的正最大值与负最小值
        """
        positiveRes=nums[0]
        negativeRes=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            positiveTemp=positiveRes*nums[i]
            negativeTemp=negativeRes*nums[i]
            positiveRes=max(positiveTemp,negativeTemp,nums[i])
            negativeRes=min(positiveTemp,negativeTemp,nums[i])
            res=positiveRes if positiveRes > res else res
        return res