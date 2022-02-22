# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        
        l3 = None
        res = None
        
        while l1 or l2:
            if not l3:
                l3 = ListNode()
                res = l3
            else:
                l3.next = ListNode()
                l3 = l3.next
            
            l1_val = 0
            l2_val = 0
            
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            
            #print(l1_val, l2_val, carry)
            temp = l1_val + l2_val + carry
            l3.val = temp%10
            carry = temp//10
        
        if carry:
            l3.next = ListNode()
            l3 = l3.next
            l3.val = carry
        
        return res
        