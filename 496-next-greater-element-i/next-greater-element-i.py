class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # i solved this not using the right approach i have used my own way but it is less efficient so i need to work in making it efficent in terms of time complexity so the thing is i need to use stack and hashtable to do it let me try my best to do it
        if not nums2:
            return None

        mydict={}
        result=[]
        stack=[]
        stack.append(nums2[0])
        for i in range(1,len(nums2)):
            while stack and stack[-1]<nums2[i]:
                mydict[stack[-1]]=nums2[i]
                stack.pop()



            stack.append(nums2[i])
# make sure that the element that didnot get any greater element mapped with -1
        for element in stack:
            mydict[element]=-1

            # finally checking all the elements in nums1 and putting it into the result array and return it
        for i in range(len(nums1)):
            result.append(mydict[nums1[i]])
        return result
        