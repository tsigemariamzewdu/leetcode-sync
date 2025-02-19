class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None



class MyLinkedList:

    def __init__(self):
        self.head=None
        
        

    def get(self, index: int) -> int:

        count=0
        cur=self.head


        while cur:
            if count==index:
                return cur.val
            cur=cur.next
            count+=1

        # while cur and count < index:
        #     cur = cur.next
        #     count += 1
        
        # if cur:
        #     return cur.val

        return -1

        

    def addAtHead(self, val: int) -> None:
        newnode=Node(val)
        newnode.next = self.head
        self.head=newnode
      
        


        # cur=self.head
        # while cur:
        #     print(cur.val)
        #     cur=cur.next

        

    def addAtTail(self, val: int) -> None:
        newnode=Node(val)
        cur=self.head

        if not cur:
            self.head = newnode
            return

        while cur and cur.next:
            cur=cur.next

        cur.next=newnode
        
        
        # c=self.head
        # while c:
        #     print(c.val)
        #     c=c.next

    def addAtIndex(self, index: int, val: int) -> None:
        
        dummy = Node(0)
        dummy.next = self.head
        newnode=Node(val)
        curr=dummy
        count=0

        while curr and count<index:
            curr=curr.next
            count+=1
        
        # temp=curr.next
    
        # curr.next=newnode
        if curr:
            newnode.next=curr.next
            curr.next=newnode
        
        self.head = dummy.next

        # c=self.head
        # while c:
        #     print(c.val)
        #     c=c.next

    def deleteAtIndex(self, index: int) -> None:
        dummy = Node(0)
        dummy.next = self.head

        curr=dummy
        count=0

        while curr and  count<index:
            curr=curr.next
            count+=1

        if curr and curr.next:  
            curr.next=curr.next.next
        
        
        self.head = dummy.next

        # c=self.head
        # while c:
        #     print(c.val)
        #     c=c.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)