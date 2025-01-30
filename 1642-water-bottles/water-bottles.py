class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result=numBottles
        total=numExchange
        while total>=numExchange:
            quotient=numBottles//numExchange
            reminder=numBottles%numExchange
            total= quotient+ reminder
            numBottles=total
            result+=quotient
        return result





       
        