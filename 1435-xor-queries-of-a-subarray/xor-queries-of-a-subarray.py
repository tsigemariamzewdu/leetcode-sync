class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXor=[arr[0]]

        for i in range(1,len(arr)):
            prefixXor.append(prefixXor[i-1]^arr[i])
        result=[]
        # print(prefixXor)

        for l,r in queries:
            if l>0:
                result.append(prefixXor[r]^prefixXor[l-1])
            else:
                result.append(prefixXor[r])
        return result