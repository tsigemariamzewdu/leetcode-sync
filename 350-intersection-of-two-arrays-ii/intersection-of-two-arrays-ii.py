class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # we can use two pointers techinique to solve this problem
        sorted_nums1=sorted(nums1)
        sorted_nums2=sorted(nums2)

        poin1=0
        poin2=0

        intersection=[]

        while poin1<len(sorted_nums1) and poin2<len(sorted_nums2):
            if sorted_nums1[poin1]==sorted_nums2[poin2]:
                intersection.append(sorted_nums1[poin1])
                poin1 +=1
                poin2 +=1
            elif sorted_nums1[poin1]>sorted_nums2[poin2]:
                poin2 +=1
            else:
                poin1 +=1
        return intersection 

        