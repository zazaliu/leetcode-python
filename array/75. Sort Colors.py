class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        startPoint,endPoint=0,len(nums)-1
        for i in range(len(nums)):
            while nums[i] == 2 and i <= endPoint:
                nums[i],nums[endPoint] = nums[endPoint],nums[i]
                endPoint-=1
            while nums[i] == 0 and i >= startPoint:
                nums[i],nums[startPoint] = nums[startPoint],nums[i]
                startPoint+=1