class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        if nums[-1] != nums[-2]: return nums[-1]
        for i in range(1,len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]

s=Solution()
nums=[1,2,1,2,3,4,5,5,4]
print(s.singleNumber(nums))