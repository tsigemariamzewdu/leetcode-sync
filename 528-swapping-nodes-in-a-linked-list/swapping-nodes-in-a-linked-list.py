# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lists=[]
        current =head
        while current:
            lists.append(current.val)
            current=current.next
        n=len(lists)
        lists[k-1],lists[n-k]=lists[n-k],lists[k-1]
        res=ListNode()
        result=res
        for i in range(n):
            res.next=ListNode(lists[i])
            res=res.next
        return result.next
        