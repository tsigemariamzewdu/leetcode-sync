# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
    #    may be i can find the middle node and reverse the second half and then check if it is the same as the first half 
        # find the middle node
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        # reverse the second half
        prev=None
        curr=slow
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode

        # the last step is to check if the first half and the second half are the same 
        left, right = head, prev
        while right:  # Only need to check until the end of the reversed half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        