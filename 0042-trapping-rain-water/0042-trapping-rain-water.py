class Solution:
    def trap(self, height: List[int]) -> int:

        ii, jj = 0, len(height)-1
        max_l = height[ii]
        max_r = height[jj]
        water = 0
        while ii<=jj:
            if max_l<=max_r:
                if height[ii]>=max_l:
                    max_l = height[ii]
                else:
                    temp = max_l-height[ii]
                    water += temp if temp>0 else temp
                ii+=1
            else:
                if height[jj]>max_r:
                    max_r = height[jj]
                else:
                    temp = max_r-height[jj]
                    water+= temp if temp>0 else 0
                jj-=1
        return water
