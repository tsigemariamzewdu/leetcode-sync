class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
      
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    box_idx = (i // 3) * 3 + j // 3
                    boxes[box_idx].add(num)
        
        def backtrack():
           
            min_candidates = 10
            best_cell = None
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        box_idx = (i // 3) * 3 + j // 3
                        candidates = set(range(1, 10)) - (rows[i] | cols[j] | boxes[box_idx])
                        num_candidates = len(candidates)
                        if num_candidates < min_candidates:
                            min_candidates = num_candidates
                            best_cell = (i, j, candidates)
                            if min_candidates == 1:  
                                break
                if min_candidates == 1:
                    break
            
            if not best_cell:  
                return True
            
            i, j, candidates = best_cell
            box_idx = (i // 3) * 3 + j // 3
            
            for num in candidates:
              
                board[i][j] = str(num)
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)
                
                if backtrack():
                    return True
                
                
                board[i][j] = '.'
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[box_idx].remove(num)
            
            return False
        
        backtrack()