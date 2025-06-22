class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        colors = set()
        color_bounds = dict()

        
        for i in range(m):
            for j in range(n):
                color = targetGrid[i][j]
                colors.add(color)
                if color not in color_bounds:
                    color_bounds[color] = [i, j, i, j]  
                else:
                    top, left, bottom, right = color_bounds[color]
                    color_bounds[color] = [
                        min(top, i),
                        min(left, j),
                        max(bottom, i),
                        max(right, j)
                    ]

       
        graph = defaultdict(set)
        indegree = defaultdict(int)

        for color in colors:
            top, left, bottom, right = color_bounds[color]
            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    other_color = targetGrid[i][j]
                    if other_color != color:
                        if color not in graph[other_color]:
                            graph[other_color].add(color)
                            indegree[color] += 1

       
        queue = deque()
        for color in colors:
            if indegree[color] == 0:
                queue.append(color)

        visited = set()
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return len(visited) == len(colors)