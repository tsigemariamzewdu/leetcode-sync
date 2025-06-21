from collections import deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
      
        max_group = m
        for i in range(n):
            if group[i] == -1:
                group[i] = max_group
                max_group += 1
        
       
        item_graph = [[] for _ in range(n)]
        item_in_degree = [0] * n
        
        group_graph = [[] for _ in range(max_group)]
        group_in_degree = [0] * max_group
        
        for i in range(n):
            for before in beforeItems[i]:
                item_graph[before].append(i)
                item_in_degree[i] += 1
                if group[before] != group[i]:
                    group_graph[group[before]].append(group[i])
                    group_in_degree[group[i]] += 1
        
        # Step 3: Topological sort of groups
        group_order = []
        group_queue = deque()
        for g in range(max_group):
            if group_in_degree[g] == 0:
                group_queue.append(g)
        
        while group_queue:
            g = group_queue.popleft()
            group_order.append(g)
            for neighbor in group_graph[g]:
                group_in_degree[neighbor] -= 1
                if group_in_degree[neighbor] == 0:
                    group_queue.append(neighbor)
        
        if len(group_order) != max_group:
            return []
        
        item_order = []
       
        group_to_items = [[] for _ in range(max_group)]
        for i in range(n):
            group_to_items[group[i]].append(i)
        
        for g in group_order:
 
            items_in_group = group_to_items[g]
            item_queue = deque()
            local_in_degree = {}
           
            for i in items_in_group:
                local_in_degree[i] = 0
            
            for i in items_in_group:
                for before in beforeItems[i]:
                    if group[before] == g:
                        local_in_degree[i] += 1
            
            for i in items_in_group:
                if local_in_degree[i] == 0:
                    item_queue.append(i)
            
            collected = 0
            while item_queue:
                current = item_queue.popleft()
                item_order.append(current)
                collected += 1
                for neighbor in item_graph[current]:
                    if group[neighbor] == g:
                        local_in_degree[neighbor] -= 1
                        if local_in_degree[neighbor] == 0:
                            item_queue.append(neighbor)
            
            if collected != len(items_in_group):
                return []
        
        return item_order