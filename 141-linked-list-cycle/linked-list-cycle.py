# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mydict={}
        current=head
        while current:
            if current in mydict:
                return True
            else:
                mydict[current]=1
            current=current.next
        return False
        
        