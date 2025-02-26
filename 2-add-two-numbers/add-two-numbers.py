# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode()
        pointer=result
       

        left=l1
        right=l2
        reminder=0

        while left or right or  reminder:
            val1=left.val if left else 0 
            val2=right.val if right else 0
            pointer.next=ListNode((val1+val2+ reminder)%10)
            reminder=(val1 +val2+ reminder)//10
            pointer=pointer.next
            left=left.next if left else None
            right=right.next if right else None
        return result.next
        