class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = {}
        r = 0
        for num in nums:
            if c.get(k-num,0):
                c[k-num] -=1
                r+=1
            else:
                c[num] = c.get(num,0)+1
        return r
        
        