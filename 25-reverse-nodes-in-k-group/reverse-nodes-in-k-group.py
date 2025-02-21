# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res=ListNode()
        curr=res
        
        cur=head
        while cur:
            prev=None
            count=0
            while cur and count<k:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
                count+=1
            
           
          
           
            print(prev)
            if count==k:
                while curr and curr.next:
                    curr=curr.next
                curr.next=prev
            else:
                prevv=None
                cu=prev
                while cu:
                    tem=cu.next
                    cu.next=prevv
                    prevv=cu
                    cu=tem
                while curr and curr.next:
                    curr=curr.next
                curr.next=prevv
                


            
            # print(res)
            
           
        
        
        return res.next      
        