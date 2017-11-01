class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left <= right:
            mid=(left+right)/2
            if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
                return nums[left]
            if nums[left] > nums[mid]:
                right=mid
            if nums[mid] > nums[right]:
                left=mid
            if left+1 == right or left == right:
                return min(nums[left],nums[right])