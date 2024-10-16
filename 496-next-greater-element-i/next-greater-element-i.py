class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        for num in nums1:
            if num in nums2:
                ind = nums2.index(num)
                found = False  # Track if we found a greater element
                for another in nums2[ind+1:]:
                    if another > num:
                        result.append(another)
                        found = True
                        break  # Stop after finding the first greater element
                if not found:
                    result.append(-1)  # Append -1 if no greater element found
        return result

        # result=[]
        # for num in nums1:
        #     if num in nums2:
        #         stack=[num]
        #         ind=nums2.index(num)
        #         for another in nums2[num:]:
        #             if another > num:
        #                 result.append(another)
        #         result.append(-1)
        # return result

        