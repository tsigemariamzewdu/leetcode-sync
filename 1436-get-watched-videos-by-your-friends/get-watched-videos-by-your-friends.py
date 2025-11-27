from collections import deque
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        graph= defaultdict(list)
        for i in range(len(friends)):
            listf=friends[i]
            for j in listf:
                graph[i].append(j)
               
        queue=deque([[id,0]])
        visited={id}

        levels_k=set()

        while queue:
            node,k=queue.popleft()
           
            if level==k:
                levels_k.add(node)
                continue
          

            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append([child,k+1])
        movies=[]
      

        for i in levels_k:
            movies.extend(watchedVideos[i])
       
        freq=Counter(movies)
        result = [v for v, c in sorted(freq.items(), key=lambda x: (x[1], x[0]))]

        return result

            
        



            
        