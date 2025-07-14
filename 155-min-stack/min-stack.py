class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.ministack=[]

        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.ministack or  val<=self.ministack[-1]:
            self.ministack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.ministack[-1]==self.stack[-1]:
            self.ministack.pop()
        self.stack.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.ministack[-1]
# so the minstack is a monotonincally decreasing stack 

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()