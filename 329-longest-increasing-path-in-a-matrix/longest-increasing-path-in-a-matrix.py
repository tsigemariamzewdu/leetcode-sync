class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        direction = [(-1,0), (0, -1), (0, 1), (1, 0)]
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n
        indegree = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                for dr, dc in direction:
                    row = r+dr
                    col =c+dc
                    if inbound(row, col) and matrix[row][col] > matrix[r][c]:
                        indegree[row][col] += 1

        queue = deque()
        distance = [[1] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if indegree[r][c] == 0:
                    queue.append((r, c))
        longest_path = 0
        while queue:
            r, c = queue.popleft()
            for dr, dc in direction:
                row = r+dr
                col = c+dc
                if inbound(row, col) and matrix[row][col] > matrix[r][c]:
                    distance[row][col] = max(distance[row][col], distance[r][c]+1)
                    indegree[row][col] -= 1

                    if indegree[row][col] == 0:
                        queue.append((row, col))
            longest_path = max(longest_path, distance[r][c])
        
        return longest_path
