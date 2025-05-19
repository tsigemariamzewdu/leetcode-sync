class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters=[]
        n=0
        for j,c in enumerate(s):
            if c.isalpha():
                n+=1
                letters.append(j)
    

        powerset=[]
        for mask in range(1<<n):
            subset=list(s)
            for i in range(n):
                if mask & (1<<i):
                    p=letters[i]
                    subset[p]=subset[p].upper()
                else:
                    p=letters[i]
                    subset[p]=subset[p].lower()
            powerset.append("".join(subset))
        return powerset
                

           
      
        