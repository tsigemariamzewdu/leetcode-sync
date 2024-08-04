class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda i : i[0])
        output=[intervals[0]] # i dont want it to be empty so that is the first list
        for s, e in intervals[1:]:
            lastend=output[-1][1] #this is the most recently added list last element we want to compare this element with the start element
            if s <= lastend:
                output[-1][1]=max(lastend,e)
            else:
                output.append([s,e])
        return output

        