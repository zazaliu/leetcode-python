# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head.next or m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        mark = dummy
        temp = None
        for i in range(m-1):
            mark = mark.next
            head = head.next
        for i in range(n-m+1):
            newNode = ListNode(head.val)
            newNode.next = temp
            temp = newNode
            head = head.next
        mark.next = temp
        while mark.next:mark = mark.next
        mark.next = head
        return dummy.next