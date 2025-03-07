class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in "+-*/":
                nums2=stack.pop()
                nums1=stack.pop()

                if i=="+":
                    stack.append(nums1+nums2)
                if i=="-":
                    stack.append(nums1-nums2)
                if i=="*":
                    stack.append(nums1*nums2)
                if i=="/":
                    if nums1*nums2<0 and nums1%nums2!=0:
                        stack.append((nums1//nums2)+1)
                    else:
                        stack.append(nums1//nums2)
            else:
                stack.append(int(i))
        return stack[0]
            

        