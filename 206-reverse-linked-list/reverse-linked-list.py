# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]

        cur=head
        while cur:
            res.append(cur.val)
            cur=cur.next
        revres=list(reversed(res))
        newnode=ListNode()
        cur=newnode
        print(revres)

        for i in range(len(revres)):
            cur.next=ListNode(revres[i])
            cur=cur.next

        return newnode.next

        