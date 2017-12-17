# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        left, right = ListNode(0), ListNode(0)
        p, p1, p2 = head, left, right
        if head.val < x:
            p1.next = ListNode(head.val)
            p1 = p1.next
        else:
            p2.next = ListNode(head.val)
            p2 = p2.next
        while p.next:
            p = p.next
            if p.val < x:
                p1.next = ListNode(p.val)
                p1 = p1.next
            else:
                p2.next = ListNode(p.val)
                p2 = p2.next
        p1.next = right.next
        return left.next

