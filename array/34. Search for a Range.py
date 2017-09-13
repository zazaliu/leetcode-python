class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right=0,len(nums)-1
        flag1,flag2=-1,-1
        while left <= right:
            if nums[left] == target:
                flag1=left
            else:
                left+=1
            if nums[right] == target:
                flag2=right
            else:
                right-=1
            if flag1 != -1 and flag2 != -1:
                return [flag1,flag2]
        return [flag1,flag2]