# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newHead = res = ListNode(0)
        res.next = head
        while newHead.next and newHead.next.next:
            p1, p2 = newHead.next, newHead.next.next
            newHead.next = p2
            p1.next = p2.next
            p2.next = p1
            newHead = newHead.next.next
        return res.next