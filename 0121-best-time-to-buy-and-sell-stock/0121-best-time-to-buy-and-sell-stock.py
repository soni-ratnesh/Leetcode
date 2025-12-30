class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        if len(prices) ==2:
            return max(0, prices[1]-prices[0])
        
        jj = len(prices)-1
        stack = []
        result = 0

        while jj>=0:
            while len(stack) and stack[-1]<prices[jj]:
                stack.pop()
            if len(stack)==0:
                stack.append(prices[jj])
  
            else:
                result = max(result, stack[-1] - prices[jj] )
            jj-=1
        return result