class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
    #    create a dictionary to store the last occurence of each char
        last_occur={}
        for i,c in enumerate(s):
            last_occur[c]=i #this makes sure that the key c is mapped with the last occurence of it and that is i
        # lets see an example if s="bcabc"
        # then {b:3,c:4 a:2}

        # now lets initalize our stack that is like a result array
        stack=[]
        # since the chars are supposed to be a uniques chars i am supposed to use a set 
        seen=set() #now i have a set element where i can add element or discord element whenever i want 

        for i ,c in enumerate(s):
            if c in seen:
                continue
            while stack and c<stack[-1] and i<last_occur[stack[-1]]:
                removed_char=stack.pop()
                seen.remove(removed_char)
            stack.append(c)
            seen.add(c)
        return ''.join(stack)
        

# 
# 

        
        

        