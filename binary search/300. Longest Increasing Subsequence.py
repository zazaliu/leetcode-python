class Solution:
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        DP算法：复杂度：O(n^2)
        """
        if not nums:return 0
        dp=[1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i]=max(dp[j]+1,dp[i])
        return max(dp)
    def lengthOfLIS(self, nums):
        """
        维护一个数组，依次二分查找当前元素在维护的数组中的位置，选择更新或者不做操作，最后所维护数组长度即为最长子序列长度
        :param nums:
        :return:
        """
        if not nums:return 0
        lis=[]
        for i in range(len(nums)):
            left,right=0,len(lis)
            while left < right:
                mid=left+(right-left)//2
                if lis[mid] < nums[i]:
                    left=mid+1
                else:
                    right=mid
            if left >= len(lis):
                lis.append(nums[i])
            else:
                lis[left]=nums[i]
        return lis





s=Solution()
nums=[10, 9, 2, 5, 3, 7, 101, 18]
print(s.lengthOfLIS(nums))