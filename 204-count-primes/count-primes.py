class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime=[True]*n
        
        if n<=2:
            return 0
        is_prime[0]=False
        is_prime[1]=False
        for i in range(2,n):
            if is_prime[i]:
                for x in range(i*i,n,i):
                    is_prime[x]=False
        count=0
        for i in range(n):
            if is_prime[i]:
                count+=1
        return count

        