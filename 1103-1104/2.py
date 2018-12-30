# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        tmp = l1.val + l2.val
        if tmp >= 10:
            result.val = tmp - 10
            carry = 1
        else:
            result.val = tmp
            carry = 0 
        p = result
        l1 = l1.next 
        l2 = l2.next    
        while l1 != None or l2 != None:
            np = ListNode(0)
            if (l1 != None and l2 != None):
                tmp = l1.val + l2.val + carry
                if tmp >= 10:
                    np.val = tmp - 10
                    carry = 1
                else:
                    np.val = tmp
                    carry = 0
                l1 = l1.next 
                l2 = l2.next
            
            elif (l1 != None and l2 == None):
                tmp = l1.val + carry
                if tmp >= 10:
                    np.val = tmp - 10
                    carry = 1
                else:
                    np.val = tmp
                    carry = 0
                l1 = l1.next
                
            else:
                tmp = l2.val + carry
                if tmp >= 10:
                    np.val = tmp - 10
                    carry = 1
                else:
                    np.val = tmp
                    carry = 0
                l2 = l2.next
                
            p.next = np
            p = p.next
            
        if (carry == 1):
            np = ListNode(1)
            p.next = np
        return result
            