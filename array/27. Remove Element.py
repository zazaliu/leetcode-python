class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lenth=len(nums)
        count=nums.count(val)
        while len(nums)>(lenth-count):
            nums.remove(val)
        return len(nums)