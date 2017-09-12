class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """solution-1
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) & 1 != 0:
            return nums1[(len(nums1)-1)/2]
        else:
            return (nums1[len(nums1)/2-1]+nums1[len(nums1)/2])/2.0
        """
        l = len(nums1) + len(nums2)
        return self.findKth(nums1, nums2, l // 2) if l % 2 == 1 else (self.findKth(nums1, nums2,l // 2 - 1) + self.findKth(nums1,nums2,l // 2)) / 2.0

    def findKth(self, m, n, k):
        if len(m) > len(n):
            m, n = n, m
        if not m:
            return n[k]
        if k == len(m) + len(n) - 1:
            return max(m[-1], n[-1])
        i = len(m) // 2
        j = k - i
        if m[i] > n[j]:
            return self.findKth(m[:i], n[j:], i)
        else:
            return self.findKth(m[i:], n[:j], j)