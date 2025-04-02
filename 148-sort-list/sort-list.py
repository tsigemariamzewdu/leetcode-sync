# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        cur=head
        while cur:
            res.append(cur.val)
            cur=cur.next
        res.sort()
        dummy=ListNode()
        result=dummy
        for i in res:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return result.next
        