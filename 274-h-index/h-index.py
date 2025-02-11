class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n=len(citations)
        count=[0]*1001
        for paper in citations:
            count[paper]+=1
        s_citations=[]
        for i in range(1001):
            s_citations.extend([i]*count[i])
        
        for i in range(n):
            if s_citations[i]>=n-i:
                return n-i
                
        return 0
      
        