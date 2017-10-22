class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        利用reach记录当前index所能到达最远距离，一旦某一个index对应的值不能使得reach到达更远，则返回false
        """
        index = 0
        reach = 0
        while index < len(nums):
            if reach < index:
                return False
            reach = max(reach, index + nums[index])
            index += 1
        return True
