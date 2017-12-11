# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        middle=len(nums)//2
        left=nums[:middle]
        right=nums[middle+1:]
        root=TreeNode(nums[middle])
        root.left=self.sortedArrayToBST(left)
        root.right=self.sortedArrayToBST(right)
        return root