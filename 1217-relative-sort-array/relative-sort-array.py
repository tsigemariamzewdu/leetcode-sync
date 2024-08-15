class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in arr2:
            while i in arr1:
                arr1.remove(i)
                result.append(i)
        arr1.sort()
        if arr1:
            for j in arr1:
                result.append(j)
        return result
        