# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
       
        less=ListNode()
        greater=ListNode()
        less_tail=less
        greater_tail=greater

        cur=head
        while cur:
            if cur.val<x:
                less_tail.next=cur
                less_tail=less_tail.next
            else:
                greater_tail.next=cur
                greater_tail=greater_tail.next
            cur=cur.next
        less_tail.next=greater.next
        greater_tail.next=None
        return less.next
        



        
        