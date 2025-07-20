class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter=Counter(tasks)
        count=0
        for i in counter:
            if counter[i]<2:
                return -1
            if counter[i]>=3:
                count += ceil(counter[i]/3)
            if counter[i]==2:
                count+=1
        return count
