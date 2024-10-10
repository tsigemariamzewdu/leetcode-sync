# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num_set=set(nums)
        dummy=ListNode(next=head)
        current=head
        prev=dummy
        while current:
            if current.val in num_set:
                prev.next=current.next
            else:
                prev=current
            current=current.next
            
            
        return dummy.next