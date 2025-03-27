class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
        def isvalid(mid,cars):
            for i in range(len(ranks)):
                # if ranks[i]>mid:
                #     return False
                if ranks[i]==mid:
                    if cars==0:
                        return True
                    cars-=1
                else:
                    if cars==0:
                        return True
                    cars-=int(sqrt((mid//ranks[i])))

               
               
            return cars<=0
            

        low=min(ranks)
        high=max(ranks)*(cars**2)

        while low<=high:
            mid=(low+high)//2
            if isvalid(mid,cars):
                high=mid-1
            else:
                low=mid+1
        return low
        
        