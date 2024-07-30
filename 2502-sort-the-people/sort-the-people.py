class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        mydict={}
        for name,height in zip(names,heights):
            mydict[height]=name
        sorted_height=sorted(mydict.keys(), reverse=True)
        newlist=[]
        for i in sorted_height:
            newlist.append(mydict[i])
        return newlist
        