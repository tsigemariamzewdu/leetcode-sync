import collections

class MyStack:

    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
      
        topp = self.queue1.popleft()
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        return topp

    def top(self) -> int:
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        topp = self.queue1.popleft()
        self.queue2.append(topp)  
        self.queue1, self.queue2 = self.queue2, self.queue1  
        return topp

    def empty(self) -> bool:
        return len(self.queue1) == 0
