class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        if len(nums) < 4:
            return result
        mark = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j] ==nums[j-1]:
                    continue
                left,right = j+1,len(nums)-1
                while left<right:
                    addSum = nums[i]+nums[j]+nums[left]+nums[right]
                    temp = [nums[i],nums[j],nums[left],nums[right]]
                    if addSum == target and temp != mark:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        mark = temp
                    if addSum < target:
                        left = left+1
                    else:
                        right = right-1
        return result