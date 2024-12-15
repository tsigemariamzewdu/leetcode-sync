class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        # i need two pointers one for num1 and the other for num2 it is still sorting and i need to put them in reverse order i guess
        n1= m-1
        n2= n-1
        k=m+n-1
        while n1>=0 and n2>=0:
            if nums1[n1]>=nums2[n2]:
                nums1[k]=nums1[n1]
                k-=1
                n1-=1
                
            else:
                nums1[k]=nums2[n2]
                k-=1
                n2-=1
        # there is another egde case that is the case where there is n and no m
        while n2>=0:
            nums1[k]=nums2[n2]
            k-=1
            n2-=1
    
       
        
            

        