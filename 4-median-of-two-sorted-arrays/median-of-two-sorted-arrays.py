class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedarr=[]
        p1=0
        p2=0
        while p1<len(nums1) and p2<(len(nums2)):
            if nums1[p1]<nums2[p2]:
                sortedarr.append(nums1[p1])
                p1+=1
            else:
                sortedarr.append(nums2[p2])
                p2+=1
        while p1<len(nums1):
            sortedarr.append(nums1[p1])
            p1+=1
        while p2<len(nums2):
            sortedarr.append(nums2[p2])
            p2+=1
        if len(sortedarr)%2==0:
            return (sortedarr[(len(sortedarr)//2)-1] + sortedarr[(len(sortedarr)//2)])/2
        return sortedarr[len(sortedarr)//2]        