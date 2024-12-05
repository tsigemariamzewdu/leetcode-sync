class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # If the character sequence doesn't match without '_', it is impossible
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        i, j = 0, 0
        
        while i < len(start) and j < len(target):
            # Skip over underscores in both strings
            if start[i] == '_':
                i += 1
                continue
            if target[j] == '_':
                j += 1
                continue
            
            # If characters match, check if the 'L' and 'R' move in the right direction
            if start[i] == target[j]:
                if start[i] == 'L' and i < j:  # 'L' cannot move right
                    return False
                if start[i] == 'R' and i > j:  # 'R' cannot move left
                    return False
                i += 1
                j += 1
            else:
                return False
        
        # Check if all characters in both strings are processed
        return True
