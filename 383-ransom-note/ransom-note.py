class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
       
        randict={}
        for i in ransomNote:
            if i in randict:
                randict[i]+=1
            else:
                randict[i]=1
        magdict={}

        for j in magazine:
            if j in magdict:
                magdict[j]+=1
            else:
                magdict[j]=1
        for key,values in randict.items():
            if key not in magdict or magdict[key]<values:
                return False
        return True
            
        