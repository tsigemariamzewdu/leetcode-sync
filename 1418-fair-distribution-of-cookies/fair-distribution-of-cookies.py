class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        cook=[0]*k
        mini=float("inf")
        
        def backtrack(idx):
            nonlocal mini
            # base case
            if idx>=len(cookies):
                mini=min(mini,max(cook))
                return
            for i in range(k):
                if cook[i]+cookies[idx]>=mini:
                    continue
                cook[i]+=cookies[idx]
                backtrack(idx+1)
                cook[i]-=cookies[idx]
        backtrack(0)
        return mini



        