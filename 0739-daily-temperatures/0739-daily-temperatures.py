class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = [0]*len(temperatures)
        s = []

        for ii in range(len(temperatures)-1,-1,-1):
            while s and temperatures[s[-1]]<=temperatures[ii]:
                s.pop()
            if s:
                r[ii] = s[-1]-ii
            s.append(ii)
        return r

        