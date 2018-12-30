# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
# 
# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#         res = p = l1
#         q = l2
#         reserved = None
#         while p and q:
#             reserved = p
#             t1 = p.next
#             t2 = q
#             q = q.next
#             p.next = t2
#             t2.next = t1
#             p = t1
#         if not p and q:
#             reserved.next = q
#         return res
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        res = tmp = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if not l1:
            tmp.next = l2
        elif not l2:
            tmp.next = l1
        return res.next
        
        
        
        
        