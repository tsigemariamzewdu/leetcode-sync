class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        items1.sort()
        items2.sort()
        result=[]
        i,j=0,0
        while i < len(items1)and j< len(items2):
            if items1[i][0]==items2[j][0]:
                result .append([items1[i][0],items1[i][1]+items2[j][1]])
                i +=1
                j +=1
            elif items1[i][0]<items2[j][0]:
                result.append(items1[i])
                i +=1
            elif items1[i][0]>items2[j][0]:
                result.append(items2[j])
                j +=1
        if i==len(items1):
            while j< len(items2):
                result.append(items2[j])
                j += 1
        if j==len(items2):
            while i< len(items1):
                result.append(items1[i])
                i += 1
        return result
        
        