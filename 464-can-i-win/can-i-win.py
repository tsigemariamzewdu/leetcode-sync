class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        n=maxChoosableInteger
        memo=[None for i in range(1<< n)]
        
        total=(n*(n+1))//2
        if total<desiredTotal:
            return False
        def summ(chosen_numbers):
            total=0
            for i in range(n):
                if (1<<i)&chosen_numbers:
                    total+=(i+1)
            return total
        def dp(chosen_numbers,cur_sum):
            if memo[chosen_numbers]!=None:
                return memo[chosen_numbers]
            for i in range(n):
                if chosen_numbers &(1<<i):
                    continue
                new_chosen=chosen_numbers |(1<<i)
                new_sum=cur_sum+(i+1)
                if new_sum>=desiredTotal:
                    memo[chosen_numbers]=True
                    return True
                next_player=dp(new_chosen,new_sum)
                if next_player==False:
                    memo[chosen_numbers]=True
                    return True
            memo[chosen_numbers]=False
            return False
        return dp(0,0)



        