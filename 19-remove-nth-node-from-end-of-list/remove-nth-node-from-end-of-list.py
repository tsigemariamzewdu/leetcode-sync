# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
         """
        dummy=ListNode()
        dummy.next=head
        #  the right pointer will be moved n steps 
        left=0
        right=dummy
        count=0

        while count<n:
            right=right.next
            count+=1
        # the left pointer will be intialized and both pointers will be moved one step a head
        left=dummy
        while right.next:
            right=right.next
            left=left.next
        if left and left.next:
            left.next=left.next.next
        
        return dummy.next


       



        