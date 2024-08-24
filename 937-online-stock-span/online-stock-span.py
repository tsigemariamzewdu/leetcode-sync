class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.result = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_span = self.stack.pop()[1]
            span += prev_span
        self.stack.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)