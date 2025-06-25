class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, k, visited):
            if k == len(word):
                return True
            if (i < 0 or i >= rows or
                j < 0 or j >= cols or
                board[i][j] != word[k] or
                (i, j) in visited):
                return False

            visited.add((i, j))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if dfs(ni, nj, k + 1, visited):
                    return True
            visited.remove((i, j))  
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        return False
