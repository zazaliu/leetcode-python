# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while head:
            if head.val != val:
                p.next = head
                p = p.next
            if not head.next and head.val == val:
                p.next = None
            head = head.next
        return dummy.next
