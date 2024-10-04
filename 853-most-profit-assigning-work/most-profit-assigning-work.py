class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        tasks=sorted(zip(difficulty,profit))
        worker.sort()
        i=0
        total=0
        maximum=0

        for w in worker:
            while i<len(tasks) and tasks[i][0]<=w:
                maximum=max(maximum,tasks[i][1])
                i+=1
            total += maximum
        return total


        