from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        temp = ""
        is_open = False  # Flag 

        for line in source:
            i = 0
            while i < len(line):
                
                if i < len(line) - 1 and line[i] == "/" and line[i + 1] == "/" and not is_open:
                    break
                
                elif i < len(line) - 1 and line[i] == "/" and line[i + 1] == "*" and not is_open:
                    is_open = True
                    i += 1  # Skip "*"
                
               
                elif i < len(line) - 1 and line[i] == "*" and line[i + 1] == "/" and is_open:
                    is_open = False
                    i += 1  # Skip the "/"
                
               
                elif not is_open:
                    temp += line[i]

                i += 1  
            
            if temp and not is_open:
                result.append(temp)
                temp = ""

        return result
