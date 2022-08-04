# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head):
        
        temp = head
        prev = None
        
        while temp:
            temp_next = temp.next
            temp.next = prev
            prev = temp
            temp = temp_next
            
        return prev
    
    def printLL(self, head, text):
        while head:
            print(head.val, end="->")
            head = head.next
        print(text)
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #self.printLL(head, "root")
        #head = self.reverseLL(head)
        #self.printLL(head)
        
        prev_tail = None
        first_head = None
        while head:
            curr_head = head
            prev = None
            
            t = k
            while t and head:
                prev = head
                head = head.next
                t -= 1
            
            if t > 0:
                if not first_head:
                    first_head = curr_head
                else:
                    prev_tail.next = curr_head
                break
            
            # break the link
            prev.next = None
            
            # self.printLL(curr_head, "curr_head")
            # self.printLL(head, "head")
            
            new_head = self.reverseLL(curr_head)
            if not first_head:
                first_head = new_head
            
            # self.printLL(new_head, "new_head")
            # self.printLL(prev_tail, "prev_tail")
            
            # join to prev rev head
            if prev_tail:
                prev_tail.next = new_head
            
            # set the curr_head as prev rev head
            prev_tail = curr_head
        return first_head