class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter=Counter(arr)
        lists=[]

        for i in counter:
            lists.append([counter[i],i])
        lists.sort()
        lists=lists[::-1]
       
        while lists and k>=lists[-1][0]:
            k-= lists[-1][0]
            lists.pop()
        return len(lists)
            
