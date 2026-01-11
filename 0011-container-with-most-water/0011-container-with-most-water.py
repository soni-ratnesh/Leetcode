class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<2:
            return 0
        left, right = 0, len(height)-1
        area = 0
        while left<right:
            new_area = (right-left)*min(height[left], height[right])
            area = max(area, new_area)
        
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area        
        