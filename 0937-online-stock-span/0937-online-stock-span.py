class StockSpanner:

    def __init__(self):

        self.ngl = []
        self.index = 1
        

    def next(self, price: int) -> int:
        count=1

        while len(self.ngl) and self.ngl[-1][0] <= price:
            _, i = self.ngl.pop()
                   
        count = self.index if len(self.ngl)==0 else self.index - self.ngl[-1][1] 
        self.ngl.append((price, self.index))
        self.index +=1

        return count
        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)