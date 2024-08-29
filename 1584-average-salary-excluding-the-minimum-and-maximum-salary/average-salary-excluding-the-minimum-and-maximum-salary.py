class Solution(object):
    def average(self, salary):
        mins = min(salary)
        maxs = max(salary)
        totl = sum(salary) - mins - maxs
        avg = totl / float(len(salary) - 2)
        return avg




    
  

        