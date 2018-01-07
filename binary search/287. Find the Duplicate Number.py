class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        复杂度：O(n^2)
        """
        for i in range(len(nums)):
            temp=nums[i]
            for j in range(i):
                if nums[j] == temp:
                    return temp
    def findDuplicate1(self, nums):
        """
        :param nums:
        :return:
        """
        """
        将nums看作链表，nums[a]=b看作a.next=b，参考Problem142，查找链表环入口即可
        """
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while fast != slow:
            fast, slow = nums[fast], nums[slow]
        return fast

    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        二分查找：首先搜索空间固定为[1，n]，每次选择1，n之间的值mid，然后遍历nums数组，记录数组中比不小于mid值的数量，记录为count，
        然后判断，如果count值大于mid，则搜索空间修改为[1,mid]，否则空间为[mid+1,n],重复以上过程，直至搜索空间变成一个数字。
        复杂度：O(nlogn)
        """
        left, right = 1, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return nums[left]




s=Solution()
nums=[1,3,4,2,2]
print(s.findDuplicate2(nums))