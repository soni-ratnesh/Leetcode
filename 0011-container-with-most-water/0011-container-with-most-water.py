class Solution:
    def maxArea(self, height: List[int]) -> int:
        ii, jj = 0, len(height)-1
        water = 0
        while ii<jj:
            water = max(water, (jj-ii )*(min(height[ii], height[jj])))

            if height[ii]>height[jj]:
                jj-=1
            else:
                ii+=1
        return water