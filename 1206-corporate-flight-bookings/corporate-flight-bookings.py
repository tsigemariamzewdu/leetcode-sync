class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix=[0]*(n+1)

        for i in range(len(bookings)):
            x,y,z=bookings[i]
            prefix[x-1]+=z
            prefix[y]-=z
        print(prefix)
        ans=[0]*n

        ans[0]=prefix[0]

        for j in range(1,len(prefix)-1):
            ans[j]=ans[j-1]+prefix[j]
        return ans
        