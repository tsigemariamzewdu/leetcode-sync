# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        
        newlist=[]
        current=head
        while current:
            newlist.append(current)
            current=current.next
        anotherlist=[]
        
        leftid=left-1
        rightid=right-1
       
        firstlist=newlist[:leftid]
        reversedthing=newlist[leftid:rightid+1]
        lastlist=newlist[rightid+1:]
        truereverse=reversedthing[::-1]
        anotherlist.extend(firstlist)
        anotherlist.extend(truereverse)
        anotherlist.extend(lastlist)
        

        # now rebuilding the linked list
        # dummy=ListNode(anotherlist[0])
        # current=dummy

        # for num in anotherlist[1:]:
        #     current.next=num
        #     current=current.next
        # return dummy

        dummy = ListNode(0)  # Create a dummy head
        current = dummy

        for node in anotherlist:  # Loop through ListNode objects
            current.next = node  # Link the next node
            current = current.next  # Move to the new node
        
        current.next = None  # Ensure the last node points to None
        return dummy.next  # Return the head of the new linked list
        





        