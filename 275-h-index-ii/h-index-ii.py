class Solution:
    def hIndex(self, citations: List[int]) -> int:

        def isvalid(mid):
            
            cited=citations[mid]
            papers=len(citations)-mid
            if  cited >= papers:
                return True
            return False


        low=0
        high=len(citations)-1


        while low<=high:
            mid=(low+high)//2
            if isvalid(mid):
                high=mid-1
            else:
                low=mid+1
        return len(citations)-low
        
       
        