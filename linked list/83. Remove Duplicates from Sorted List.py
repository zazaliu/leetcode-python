# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        flag = head
        step = head
        listVal = {}
        while step != None:
            if step.val in listVal:
                flag.next = flag.next.next
            else:
                listVal[step.val] = True
                flag = step
            step = step.next
        return head