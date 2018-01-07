class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        """
        O(n)解法
        """
        total = left = 0
        result = len(nums)+1
        for right, value in enumerate(nums):
            total += value
            while total >= s:
                result = min(result, right-left+1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0

    def minSubArrayLen1(self, s, nums):
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left, result = 0, len(nums)+1
        for right, value in enumerate(nums):
            if value >= s:
                left = self.helpFindLeft(nums, left, right, value, s)
                result = min(result, right-left+1)
        return result if result <= len(nums) else 0
    def helpFindLeft(self, nums, left, right, value, s):
        while left < right:
            mid = left+(right-left)//2
            if value-nums[mid] >= s:
                left = mid+1
            else:
                right = mid
        return left





s = Solution()
s1 = 7
nums = [2, 3, 1, 2, 4, 3]
print(s.minSubArrayLen1(s1, nums))