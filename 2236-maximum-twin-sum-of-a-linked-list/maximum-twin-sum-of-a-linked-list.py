# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res=float("-inf")

        right=head
        cur=head

        count=0
        while cur:
            count+=1
            cur=cur.next
        
        prev=None
        cur=head

        countt=0
        while cur and countt<count//2:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            countt+=1
        pointerprev=prev
        pointercur=cur
        

        res=float("-inf")
        while pointerprev and pointercur:
            res=max(res,pointerprev.val+pointercur.val)
            pointerprev=pointerprev.next
            pointercur=pointercur.next
        return res


            
        