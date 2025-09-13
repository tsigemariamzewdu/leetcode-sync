class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels={"a","e","i","o","u"}
        vowels_list=[]
        cons_list=[]
        for i in s:
            if i in vowels:
                vowels_list.append(i)
            else:
                cons_list.append(i)
        ans=0
        if vowels_list:
            counterv=Counter(vowels_list)
            maxi=0
            for j in counterv:
                maxi=max(maxi,counterv[j])
            ans+=maxi
        if cons_list:
            counterc=Counter(cons_list)
            maxi=0
            for k in counterc:
                maxi=max(maxi,counterc[k])
            ans+= maxi
        return ans



        