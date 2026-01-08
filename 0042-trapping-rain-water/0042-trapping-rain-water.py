class Solution:
    def trap(self, height: List[int]) -> int:
        lr = [height[-1]]*len(height)

        for ii in range(len(height)-2,-1,-1):
            lr[ii] = max(lr[ii+1], height[ii])
        water = 0
        max_left = height[0]
        for ii in range(1,len(height)):

            water += 0 if min(max_left, lr[ii]) - height[ii] <0 else min(max_left, lr[ii]) - height[ii]

            if max_left<height[ii]:
                max_left = height[ii]
        
        return water