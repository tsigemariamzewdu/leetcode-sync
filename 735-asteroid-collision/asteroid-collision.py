class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
     
        stack = []
        for astero in asteroids:
            while stack and astero < 0 and stack[-1] > 0:
                if stack[-1] < -astero:
                    stack.pop()
                    continue
                elif stack[-1] == -astero:
                    stack.pop()
                break
            else:
                stack.append(astero)
        return stack