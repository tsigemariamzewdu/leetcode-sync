class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        mini=float("inf")
       
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]< mini:
                mini=arr[i+1]-arr[i]
         
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==mini:
                res.append([arr[i],arr[i+1]])
        return res

