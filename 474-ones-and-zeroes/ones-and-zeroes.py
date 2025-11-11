class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeros=[s.count('0') for s in strs]
        ones=[s.count('1') for s in strs]
        memo={}
      
        def dp(rz,ro,curr_ind):
            if curr_ind==len(strs):
                return 0

            if (rz,ro,curr_ind) not in memo:
                skip=dp(rz,ro,curr_ind+1)

                take=0
                if rz >= zeros[curr_ind] and ro >= ones[curr_ind]:
                    take = 1+ dp(rz-zeros[curr_ind],ro-ones[curr_ind],curr_ind+1)
                res=max(skip,take)
                memo[(rz,ro,curr_ind)]=res
            return memo[(rz,ro,curr_ind)]
        return dp(m,n,0)
            