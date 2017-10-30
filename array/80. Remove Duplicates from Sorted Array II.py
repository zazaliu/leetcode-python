class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        遍历list，设置初始值start值与出现次数count，将不满足条件的值设置为字符串“0”，然后删除list中所有字符串“0”
        即可
        """
        if not nums:
            return 0
        start = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == start:
                count += 1
                if count > 2:
                    nums[i] = '0'
            else:
                start = nums[i]
                count = 1
        while nums.count('0'):
            nums.remove('0')
        return len(nums)