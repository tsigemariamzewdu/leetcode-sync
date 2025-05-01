# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for li in lists:
            current=li
            while current:
                heappush(heap,current.val)
                current=current.next
        res=ListNode()
        result=res
        while heap:
            res.next=ListNode(heappop(heap))
            res=res.next
        return result.next
        