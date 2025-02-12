class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        i=0
        j=0
        res=0

        while i<len(seats) and j< len(students):
            res+=abs(students[i]-seats[j])
            i+=1
            j+=1
        return res
        
        