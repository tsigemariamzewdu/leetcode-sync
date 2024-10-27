from collections import deque

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        #  Initialize the queue with characters having frequency 1
        q = deque()
        for i, char in enumerate(s):
            if frequency[char] == 1:
                q.append((char, i))

        #  Process the queue
        while q:
            char, idx = q.popleft()  
            if frequency[char] == 1:
                return idx

        return -1
