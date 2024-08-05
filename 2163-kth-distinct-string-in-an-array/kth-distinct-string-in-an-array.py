class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        newlist=[]
        mydict={}
        for i in arr:
            if i  in mydict:
                mydict[i]+=1
            else:
                mydict[i]=1
        for i in arr:
            if mydict[i]==1:
                newlist.append(i)
        if k <= len(newlist):
            return newlist[k-1]
        else:
            return ""

        
    