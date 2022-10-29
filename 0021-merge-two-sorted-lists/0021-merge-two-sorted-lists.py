# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = None
        temp = None
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        
        while list1 and list2:
            
            val = None
            
            if list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
                
            if not res:
                res = ListNode(val)
                temp = res
            else:
                res.next = ListNode(val)
                res = res.next
        
        node = None
        
        if list1:
            node = list1
        
        if list2:
            node = list2
        
        if res:
            res.next = node
        else:
            res = node
            
        return temp