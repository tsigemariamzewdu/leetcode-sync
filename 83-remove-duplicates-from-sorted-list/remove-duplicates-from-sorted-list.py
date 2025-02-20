# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left=head

        while  left :
            while  left.next and left and left.next.val==left.val:
                left.next=left.next.next
            left=left.next
            
            
        return head
        