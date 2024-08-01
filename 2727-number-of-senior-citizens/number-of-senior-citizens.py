class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count=0
        for detail in details:
            if int(detail[11:13])>60:
                count +=1
        return count
        