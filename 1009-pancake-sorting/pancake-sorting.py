class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res=[]
        n=len(arr)
        for i in range(n,0,-1):
            while i!=arr[i-1]:
                if i==arr[0]:
                    arr[:i]=reversed(arr[:i])
                    res.append(i)
                else:
                    j=arr.index(i)
                    arr[:j+1]=reversed(arr[:j+1])
                    res.append(j+1)
        return res
            
            
               
        print(res)
                    
                





        