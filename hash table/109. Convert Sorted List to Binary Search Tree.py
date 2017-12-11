# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        return self.DFS(res)
    def DFS(self,nums):
        if not nums:
            return None
        middle=len(nums)//2
        left=nums[:middle]
        right=nums[middle+1:]
        root=TreeNode(nums[middle])
        root.left=self.DFS(left)
        root.right=self.DFS(right)
        return root