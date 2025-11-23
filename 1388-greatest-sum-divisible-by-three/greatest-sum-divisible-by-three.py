class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total=sum(nums)
        rem=total%3
        list1=[]
        list2=[]
        for num in nums:
            if num%3==1:
                list1.append(num)
            elif num%3 ==2:
                list2.append(num)
        list1.sort(reverse= True)
        list2.sort(reverse=True)

        if rem ==0:
            return total
        else:
        
            if rem==1:
                if list1:
                    elem=list1.pop()
                    cand=float("inf")
                    if len(list2)>=2:
                        elem1=list2[-1]
                        elem2=list2[-2]
                        cand = elem1+elem2

                    total-= min(elem,cand)
                elif len(list2)>=2:
                        elem1=list2[-1]
                        elem2=list2[-2]
                        total  -= elem1+elem2
            else:
                if list2:
                    elem=list2.pop()
                    cand=float("inf")
                    if len(list1)>=2:
                        elem1=list1[-1]
                        elem2=list1[-2]
                        cand = elem1+elem2
                    total-=min(cand,elem)
               
                elif len(list1)>=2:
                        elem1=list1[-1]
                        elem2=list1[-2]
                        total -= elem1+elem2
        return total
        