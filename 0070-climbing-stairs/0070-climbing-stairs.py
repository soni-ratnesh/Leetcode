
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 2:
            return n

        steps = [0]*n

        steps[0] = 1
        steps[1] = 2
       
        for ii in range(2, n):
            steps[ii] = steps[ii-1]+steps[ii-2]
        return steps[-1]