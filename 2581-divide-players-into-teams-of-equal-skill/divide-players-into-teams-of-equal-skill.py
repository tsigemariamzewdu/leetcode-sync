class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
       
        skill.sort()
        left = 0
        right = len(skill) - 1
        condition = skill[left] + skill[right] 
        
        summ = 0
        while left < right:
            pro = skill[left] * skill[right]
            if skill[left] + skill[right] == condition:
                summ += pro
                left += 1
                right -= 1
            else:
                return -1
        return summ


        