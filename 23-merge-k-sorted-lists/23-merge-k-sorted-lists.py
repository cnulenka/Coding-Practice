# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = None
        head = None
        
        heap = []
        k = len(lists)
        
        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while heap:
            val, ind = heapq.heappop(heap)
            # print(val, ind)
            
            if not res:
                res = ListNode(val)
                head = res
            else:
                res.next = ListNode(val)
                res = res.next
            
            if lists[ind]:
                heapq.heappush(heap, (lists[ind].val, ind))
                lists[ind] = lists[ind].next
                
        
        return head
            
        
        
        