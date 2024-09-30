class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = ""
        for i in digits:
            sum = sum + str(i)
        newSum = int(sum) + 1
        newList = []
        for i in str(newSum):
            newList.append(int(i))
        return newList

