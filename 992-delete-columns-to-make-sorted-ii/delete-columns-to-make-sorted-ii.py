class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        if not strs:
            return 0
        
        rows =len(strs)
        cols =len(strs[0])
        
      
        sorted_pairs =[False]*(rows - 1)
        
        deletions = 0
        
        for c in range(cols):
       
            need_delete = False
            for r in range(rows - 1):
                if not sorted_pairs[r] and strs[r][c] > strs[r+1][c]:
                    need_delete = True
                    break
            
            if need_delete:
                deletions += 1
            else:
             
                for r in range(rows - 1):
                    if not sorted_pairs[r] and strs[r][c] < strs[r+1][c]:
                        sorted_pairs[r] = True
        
        return deletions