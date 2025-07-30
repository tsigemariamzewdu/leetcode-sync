class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        mapp=defaultdict(list)

        for i in range(len(ring)):
            mapp[ring[i]].append(i)
        
        queue=deque([[0,0]]) 
        
        for c in key:
            temp_list=[]
            while queue:
                pos,cost=queue.popleft()
                temp_list.append([pos,cost])
            print(temp_list)

            map_list=mapp[c]
            for j in range(len(map_list)):
                mini=float("inf")
                
                for pos,cost in temp_list:
                    m=min(abs(pos - map_list[j])+cost, len(ring) - abs(pos - map_list[j])+cost)
                    mini=min(m,mini)
                queue.append([map_list[j],mini+1])
        # print(queue)     
        res_lists=[]
        while queue:
            pos,cost=queue.popleft()
            res_lists.append(cost)
        return min(res_lists)
        


        
        