class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=[]
        for i in tokens:
            if i in "+-*/":
                nums2=res.pop()
                nums1=res.pop()

                if i=="+":
                    res.append(nums1+nums2)
                if i=="-":
                    res.append(nums1-nums2)
                if i=="*":
                    res.append(nums1*nums2)
                if i=="/":
                    if nums1*nums2<0 and nums1%nums2!=0:
                        res.append((nums1//nums2)+1)
                    else:
                        res.append(nums1//nums2)
            else:
                res.append(int(i))
        return res[0]
            

        