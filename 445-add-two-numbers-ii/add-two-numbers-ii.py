# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # let me use a reverse function and reverse both lists and then 
        # the lists [3,4,2,7] and  [4,6,5]
       
        def reverselist(head):
       
            prev=None

            current=head
            while current is not None:
                nxt=current.next
                current.next=prev
                prev=current
                current=nxt
            return prev
        # the reversed lists are now
        l1rev=reverselist(l1)
        l2rev=reverselist(l2)

        remainder=0
        dummy = ListNode(0)  
        current = dummy

        while l1rev or l2rev or remainder:
            val1=l1rev.val if l1rev else 0
            val2=l2rev.val if l2rev else 0


            total= val1 + val2 + remainder
            remainder=total//10
            true_val=total%10

            current.next=ListNode(true_val)
            current=current.next

            if l1rev: l1rev=l1rev.next
            if l2rev: l2rev=l2rev.next

        return reverselist(dummy.next)

       
        
        
        
            

        