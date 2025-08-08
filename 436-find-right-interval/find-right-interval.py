class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        withindex=[]
        for i in range(len(intervals)):
            withindex.append((intervals[i][0],intervals[i][1],i))
     
        res=[-1]*(len(intervals))

        sortedintervals=sorted(withindex) 
        for s,e,ind in sortedintervals:
            low=0
            high=len(intervals)-1

            while low<=high:
                mid=(low+high)//2
                if sortedintervals[mid][0]>=e:
                    high=mid-1
                else:
                    low=mid+1
            if low<len(intervals):
                res[ind]=sortedintervals[low][2]
        return res

            

        


        