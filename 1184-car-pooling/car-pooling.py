class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix=[0]*1001

        for trip in trips:
            n=trip[0]
            s=trip[1]
            e=trip[2]

            prefix[s]+=n
            prefix[e]-=n
        prefixsum=[0]*1001
        prefixsum[0]=prefix[0]
        for i in range(1,len(prefix)):
            prefixsum[i]=prefixsum[i-1]+prefix[i]
        for j in prefixsum:
            if j>capacity:
                return False
        return True
