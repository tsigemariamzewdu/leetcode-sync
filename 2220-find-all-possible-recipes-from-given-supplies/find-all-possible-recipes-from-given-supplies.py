class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        incoming=defaultdict(int)

        supply_set=set(supplies)
        for i in range(len(recipes)):
            recipe = recipes[i]
            for ing in ingredients[i]:
                graph[ing].append(recipe)
                incoming[recipe] += 1

        # print(graph)
        # print(incoming)
        q=deque(supplies)

        result=[]

        while q:
            item=q.popleft()

            for i in graph[item]:
                incoming[i]-=1
                if incoming[i]==0:
                    q.append(i)
                    result.append(i)
        return result
            

