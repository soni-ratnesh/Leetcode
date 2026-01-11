class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) ==1:
            return [nums[0]**2]
        else:
            # find first positive:
            for pos in range(len(nums)):
                if nums[pos]>=0:
                    break
            
            neg = pos-1
            result = []
            while 0<=neg or pos<len(nums):
                n_val = float('Inf') if neg<0 else nums[neg]
                p_val =  float('Inf') if pos>=len(nums) else nums[pos]

                if abs(n_val)<abs(p_val):
                    result.append(n_val**2)
                    neg-=1
                else:
                    result.append(p_val**2)
                    pos+=1
            return result