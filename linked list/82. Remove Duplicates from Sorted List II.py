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
        """
        先按照 Remove Duplicates from Sorted List 的方法把重复的数字减至一个，
        接下来要考虑怎样可以把这一个节点也删除，那么只要在前一个节点对当前节点去重后，
        再把前一个节点的指针指向当前节点的后一个节点。因为要通过当前节点的前一个节点来
        操作，所以加了一个假的头节点。而如果节点没有重复的话不需要跳过当前节点，所以要
        一个额外的变量来记录当前节点是否有重复节点。
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        flag = False
        while cur.next:
            while cur.next.next and cur.next.next.val == cur.next.val:
                cur.next = cur.next.next
                flag = True
            if flag:
                cur.next = cur.next.next
                flag = False
            else:
                cur = cur.next
        return dummy.next
