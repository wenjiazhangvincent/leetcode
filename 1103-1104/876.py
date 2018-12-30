# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        count = 0
        p = head
        while p.next:
            p = p.next
            count += 1
        for i in range((count+1)/2):
            head = head.next
        return head