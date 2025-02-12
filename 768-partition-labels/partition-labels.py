import copy
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res=[]
        mydict={}
        for i in range(len(s)):
           mydict[s[i]]=i
        

        left=0
        right=mydict[s[0]]
        while right<len(s):
            while mydict[s[left]]<=right and left<right:
                left+=1
                if  mydict[s[left]]>right:
                    right=mydict[s[left]]
        
            res.append(right+1)
            
            if right+1<len(s):
                left=right+1
                right=mydict[s[left]]
            else:
                break
        c_res=copy.deepcopy(res)
        for i in range(len(res)):
            if i==0:
                res[i]=c_res[i]
            else:
                res[i]=c_res[i]-c_res[i-1]
        return res
                


       

           
        