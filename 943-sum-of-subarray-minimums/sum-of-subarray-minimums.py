class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        back=[0]*len(arr)
        front=[0]*len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            back[i]=i-stack[-1] if stack else i+1
            stack.append(i)
        stack=[]

        for j in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>arr[j]:
                stack.pop()
            front[j]=stack[-1]-j if stack else len(arr)-j
            stack.append(j)
       

        result=0 

        for k in range(len(arr)):
            result+=arr[k]*back[k]*front[k]
            result %=((10**9)+7)
        return result



        
            

        

       
            

        
        