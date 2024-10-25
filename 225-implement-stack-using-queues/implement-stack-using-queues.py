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
        # Get the last element (top of the stack)
        topp = self.queue1.popleft()
        # Swap the queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        return topp

    def top(self) -> int:
        # Use pop to retrieve the top element, but push it back to queue1
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        topp = self.queue1.popleft()
        self.queue2.append(topp)  # Put the top element back in queue2
        self.queue1, self.queue2 = self.queue2, self.queue1  # Swap again
        return topp

    def empty(self) -> bool:
        return len(self.queue1) == 0

