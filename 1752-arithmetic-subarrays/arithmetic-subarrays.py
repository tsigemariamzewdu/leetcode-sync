class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result=[0]*len(l)
        for i in range(len(l)):
            
            curnum=nums[l[i]:r[i]+1]
            curnum.sort()
            diff=curnum[0]-curnum[1]
            print(diff)
            for j in range(1,len(curnum)-1):
                curdiff=curnum[j]-curnum[j+1]
                print(curdiff)
                if curdiff!=diff:
                    result[i]=False
                   
                    break
            else:
                result[i]=True
        #
        return result




            
        