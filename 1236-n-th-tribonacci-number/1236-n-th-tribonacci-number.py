class Solution:
    def tribonacci(self, n: int) -> int:
        r = [0,1,1]
        if n<3:
            return r[n]
        
        for ii in range(3,n+1):
            r = [r[1], r[2], r[0]+r[1]+r[2]]
        
        return r[2]