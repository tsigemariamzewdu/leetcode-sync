class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dictt=defaultdict(int)
        count=0
        for n in arr:
            dictt[n%k]+=1
        # print(dictt)
        for n in range(1,k):
            if n==k-n and dictt[n]&1:
                return False
            if dictt[n]!=dictt[k-n]:
                return False
        return True

       