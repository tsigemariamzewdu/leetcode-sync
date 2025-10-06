class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dictt=defaultdict(int)
        count=0
        for n in arr:
            dictt[n%k]+=1
        print(dictt)
        for n in arr:
            if n%k==0 and dictt[n%k]>=2:
                count+=1
                dictt[n%k]-=2
            elif (dictt[k-(n%k)]>0  and dictt[n%k]>0):
                dictt[n%k]-=1
                if dictt[k-(n%k)]>0:
                    dictt[k-(n%k)]-=1
                    count+=1

        print(count)
        return count==(len(arr)//2)
          



        print(dict)

        