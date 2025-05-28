class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1=Counter(words1)
        counter2=Counter(words2)

        wordset=set()
        for i in words1:
            wordset.add(i)
        for j in words2:
            wordset.add(j)
        count=0
        for i in wordset:
            if counter1[i]==1 and counter2[i]==1:
                count+=1
        return count



        