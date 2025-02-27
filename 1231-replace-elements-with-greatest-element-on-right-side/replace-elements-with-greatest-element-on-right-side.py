class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            return [-1]
        maxi=arr[-1]
        arr[-1]=-1
        for i in range(len(arr)-2,-1,-1):
            cur=arr[i]
            arr[i]=maxi
            if cur>maxi:
                maxi=cur
        return arr
            
       
        