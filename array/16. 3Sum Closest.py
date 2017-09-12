class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        bestSum = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j,k = i+1,len(nums)-1
            while j<k:
                addSum = nums[i]+nums[j]+nums[k]
                if addSum == target:
                    return addSum
                if abs(addSum-target) < abs(bestSum-target):
                    bestSum = addSum
                if addSum < target:
                    j = j+1
                else:
                    k = k-1
        return bestSum