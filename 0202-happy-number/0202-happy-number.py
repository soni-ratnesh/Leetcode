class Solution:
    def isHappy(self, n: int) -> bool:
        def calHappy(n):
            r = 0
            while n:
                n, l = divmod(n,10)
                r+=l**2
            return r
        
        if n==1 :
            return True
        
        visited = set()

        while n:
            if n==1:
                return True
            elif n in visited:
                return False
            else:
                visited.add(n)
                n = calHappy(n)