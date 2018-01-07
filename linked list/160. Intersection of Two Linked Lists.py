# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """
        先计算两个单链表长度，利用两个指针，先让长度更长的单链表前进两者长度差的步数，然后两个指针同步前进，比较是否相等即可
        """
        if not headA or not headB:
            return None
        lenA = lenB = 1
        pointA, pointB = headA, headB
        while headA.next:
            headA = headA.next
            lenA += 1
        while headB.next:
            lenB += 1
            headB = headB.next
        if lenA > lenB:
            for i in range(lenA-lenB):
                pointA = pointA.next
        else:
            for i in range(lenB-lenA):
                pointB = pointB.next
        while pointA != pointB:
            pointA, pointB = pointA.next, pointB.next
        return pointA

    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """
        不用计算两个链表长度，利用两个指针遍历两个单链表，当一个链表遍历完成，则将指针之向另一个链表，如果有交点，则两指针会相遇
        """
        if not headA or not headB:
            return None
        pointA, pointB = headA, headB
        while pointA != pointB:
            pointA = pointA.next if pointA else headB
            pointB = pointB.next if pointB else headA
        return pointA