class ProductOfNumbers:

    def __init__(self):
        
        
        self.prefix=[1]
        self.length=0

    def add(self, num: int) -> None:
       
       
        if num==0:
            self.prefix=[1]
            self.length=0
        else:
            self.prefix.append(self.prefix[self.length]*num)
            self.length+=1
           

        
        



        
        

    def getProduct(self, k: int) -> int:
        if k>self.length:
            return 0
        
        return self.prefix[self.length]//self.prefix[self.length-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)