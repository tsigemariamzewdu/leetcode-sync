class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels="aeiouAEIOU"
        svowels=[]
        for i in s:
            if i in vowels:
                svowels.append(i)
        svowels.sort()
        result=[]
        k=0
        for j in s:
            if j not in vowels:
                result.append(j)
            else:
                result.append(svowels[k])
                k+=1
        return "".join(result)
        

        