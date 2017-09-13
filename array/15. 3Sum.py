class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        if len(nums) < 3:
            return result
        addSum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                addSum = nums[i] + nums[j] + nums[k]
                if addSum < 0:
                    j = j + 1
                elif addSum > 0:
                    k = k - 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j = j + 1
                    while j < k and nums[k] == nums[k - 1]:
                        k = k - 1
                    j = j + 1
                    k = k - 1

        return result