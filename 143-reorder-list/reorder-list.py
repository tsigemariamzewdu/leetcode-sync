
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next: 
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            
            first, second = tmp1, tmp2
