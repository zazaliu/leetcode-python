class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos=-1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                pos=i-1
                break
        if pos == -1:
            nums.reverse()
            return
        else:
            for j in range(len(nums)-1,pos,-1):
                if nums[j] > nums[pos]:
                    nums[pos],nums[j]=nums[j],nums[pos]
                    break
        nums[pos+1:]=nums[pos+1:][::-1]
        return