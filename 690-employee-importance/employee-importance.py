"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph=defaultdict(list)
        idimp=defaultdict(int)

        for emplo in employees:
         
            idimp[emplo.id]=emplo.importance
            graph[emplo.id].extend(emplo.subordinates)
        ans= idimp[id]
       
        def dfs(node):
            nonlocal ans
            for child in graph[node]:
                ans+=idimp[child]
                dfs(child)
            return ans
        return dfs(id)