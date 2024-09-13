class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
    # s="ababcbaca defegde hijhklij"
    #  the first step to create a dictionary to store the last occurence of the str
        last_occur={}
        for i,char in  enumerate(s):
            if  char in s:
                last_occur[char]=i
    # now lets intialize variables
        result=[]
        start=0
        end=0

        for i,char in enumerate(s):
            end=max(end,last_occur[char])

            if i==end:
                result.append(i-start+1)
                start= i+1
        return result

