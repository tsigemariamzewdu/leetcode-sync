# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        count=0
        while cur:
            count+=1
            cur=cur.next
        if count<3:
            return head
        oddb=head

        evenb=head.next if head else None
        co=oddb
        ce=evenb

        for _ in range(count//2):
            co.next=co.next.next if co.next else None
            ce.next=ce.next.next if ce.next else None

            ce=ce.next
            if co and co.next:
                co=co.next 
        
        co.next=evenb
        return oddb


            
       


        