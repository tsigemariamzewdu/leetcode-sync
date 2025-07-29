import copy
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result=[]
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
        
            result.append(right+1)
            
            if right+1<len(s):
                left=right+1
                right=mydict[s[left]]
            else:
                break
        c_result=copy.deepcopy(result)
        for i in range(len(result)):
            if i==0:
                result[i]=c_result[i]
            else:
                result[i]=c_result[i]-c_result[i-1]
        return result
                


       

           
        