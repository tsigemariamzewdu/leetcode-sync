# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddlist=ListNode()
        evenlist=ListNode()

        oddpointer=oddlist
        evenpointer=evenlist

        count=1
        cur=head
        while cur:
            if count%2==0:
                evenpointer.next=cur
                evenpointer=evenpointer.next
            else:
                oddpointer.next=cur
                oddpointer=oddpointer.next
            cur=cur.next
            count+=1
        oddpointer.next=evenlist.next
        evenpointer.next=None
        return oddlist.next


        