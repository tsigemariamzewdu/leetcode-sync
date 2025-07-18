class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[0]*len(nums1)
        
        nums1.sort()
        nums2=[[num,i] for i,num in enumerate(nums2)]
       
        nums2.sort()

        i=0
        j=0

        unusedlist=[]
        

        while i<len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j][0]:
                res[nums2[j][1]]=nums1[i]
                i+=1
                j+=1
                # print(res)
            else:
                unusedlist.append(nums1[i])
                i+=1
        k=0
        while j<len(nums2):
            res[nums2[j][1]]=unusedlist[k]
            k+=1
            j+=1
        return res

