class Solution:
    def maxArea(self, height: List[int]) -> int:
        ii=0
        jj = len(height)-1
        r = 0
        while ii<jj:
            r = max(r, min(height[jj],height[ii])*(jj-ii))

            if height[jj]>height[ii]:
                ii+=1
            else:
                jj-=1
        return r

        