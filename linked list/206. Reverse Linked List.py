# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp = ListNode(head.val)
        while head.next:
            head = head.next
            res = ListNode(head.val)
            res.next = temp
            temp = res
        return temp