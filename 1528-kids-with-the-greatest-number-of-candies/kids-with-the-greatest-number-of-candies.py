class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        for i in range(len(candies)):
            candies[i]+=extraCandies
        result=[]
        for j in candies:
            if j >=maxi:
                result.append(True)
            else:
                result.append(False)
        return result
        