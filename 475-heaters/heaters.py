class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        def is_valid(mid):
            p1=0
            p2=0

            while p1<len(houses) and p2<len(heaters):
                if abs(houses[p1]-heaters[p2])<=mid:
                    p1+=1
                else:
                    p2+=1
            while p1<len(houses):
                if abs(houses[p1]-heaters[-1])>mid:
                    return False
            return True




        low = 0 
        high = max(max(heaters),max(houses))
        ans = high
        while high >= low :
            mid =(low+high)//2

            if is_valid(mid):
                ans = mid
                high = mid-1

            else:
                low = mid+1
        return ans      
