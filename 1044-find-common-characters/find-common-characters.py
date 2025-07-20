class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter=Counter(words[0])

        for i in range(1,len(words)):
            newcounter=Counter(words[i])
            # print(newcounter)
            for j in counter:
                if j in newcounter:
                    counter[j]=min(counter[j],newcounter[j])
                    
                else:
                    counter[j]=0
        res=[]
        for i in counter:
            for j in range(counter[i]):
                res.append(i)
        return res