# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # n = n + 1
        
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        p1, p2 = head, head
        
        i = 1
        while i <= n+1:
            p1 = p1.next
            i += 1
            
        #print(p1.val) 
            
        # if p1 == None:
        #     # delete head
        #     head = head.next
        #     return head
           
        # print(p1.val)    
        while p1:
            p1 = p1.next
            p2 = p2.next
            
        # print(p1.val, p2.val)
        p2.next = p2.next.next
        
        return head.next
            
        
        