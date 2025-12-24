class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total=sum(apple)
        capacity.sort(reverse=True)
        count=0
        for i in capacity:
            if total<=0:
                return count
            total-=i
            count+=1
        return count
            
        