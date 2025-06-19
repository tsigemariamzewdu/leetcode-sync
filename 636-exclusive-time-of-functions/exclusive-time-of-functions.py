class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result=[0]*n

        stack=[]
        prevtime=0

        for log in logs:
            i,t,time=log.split(":")

            i=int(i)
            time=int(time)

            if t=="start":
                if stack:
                    result[stack[-1]]+= time-prevtime
                stack.append(i)
                prevtime=time
            else:
                result[stack.pop()] += time-prevtime +1
                prevtime =time+1
        return result
