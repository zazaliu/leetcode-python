# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        headAdd=ListNode(0)
        headAdd.next=head
        p,length=head,1
        while p.next:
            p=p.next
            length+=1
        p.next=head         # 转换为循环链表
        step=length-(k%length)
        for i in range(step):
            p=p.next
        res=p.next
        p.next=None
        return res