class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = 0,0
        ii, jj = 0, len(height)-1
        water = 0
        while ii<=jj:
            if max_left<=max_right:
                if height[ii]>=max_left:
                    max_left = height[ii]
                else:
                    water += max_left-height[ii]
                ii+=1
            else:
                if height[jj]>=max_right:
                    max_right = height[jj]
                else:
                    water += max_right - height[jj]
                jj-=1
        return water