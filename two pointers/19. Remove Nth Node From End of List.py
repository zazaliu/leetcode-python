# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        加一个头结点headAdd，并使用双指针p1和p2。p1先向前移动n个节点，
        然后p1和p2同时移动，当p1.next==None时，此时p2.next指的就是需要删除的节点。
        """
        headAdd=ListNode(0)
        headAdd.next=head
        p1,p2=headAdd,headAdd
        for i in range(n):
            p1=p1.next
        while p1.next:
            p1=p1.next
            p2=p2.next
        p2.next=p2.next.next
        return headAdd.next