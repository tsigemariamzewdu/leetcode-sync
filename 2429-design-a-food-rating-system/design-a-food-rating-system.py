
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisinestofood=defaultdict(list)
        self.cuisines={}
        self.ratings={}

        for i in range(len(foods)):
           
            self.cuisines[foods[i]]=cuisines[i]
            self.ratings[foods[i]]=ratings[i]
            heapq.heappush(self.cuisinestofood[cuisines[i]],(-ratings[i],foods[i]))


        

    def changeRating(self, food: str, newRating: int) -> None:
        c=self.cuisines[food]

        self.ratings[food]=newRating
        heapq.heappush(self.cuisinestofood[c], (-newRating,food)) 

        

    def highestRated(self, cuisine: str) -> str:
        heap=self.cuisinestofood[cuisine]
    
        while heap:
            rating,food=heap[0]
            if -rating==self.ratings[food]:
                return food
            heapq.heappop(heap)


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)