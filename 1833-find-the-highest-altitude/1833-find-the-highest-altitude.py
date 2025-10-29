class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        r=0
        curr_sum = 0

        for ele in gain:
            curr_sum += ele
            r= max(r,curr_sum)
        return r
        