class Solution:
    def smallestNumber(self, pattern: str) -> str:
        path=[]
        ans=[]

        def is_pattern(patt):
    
            for i in range(len(pattern)):
                if pattern[i]=="D":
                    if int(patt[i])>int(patt[i+1]):
                        continue
                    else:
                     
                        return False

                else:
                    if  int(patt[i])<int(patt[i+1]):
                        continue

                    else:
                      
                        return False
               
            return True






        def backtrack(idx):
            if len(path)==len(pattern)+1:
                if is_pattern(path[:]):
                
                    ans.append("".join(path[:]))
                return
           


            for i in range(1,len(pattern)+2):
                if ans:
                    return 
                if str(i) not in path:
                    path.append(str(i))
                    backtrack(idx+1)
                    path.pop()


        backtrack(1)
        return ans[0]