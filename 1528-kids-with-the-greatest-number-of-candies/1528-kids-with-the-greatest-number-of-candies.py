class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ele = candies[0]
        for ele in candies:
            if max_ele < ele:
                max_ele = ele
        
        result = []
        for ele in candies:
            result.append(ele+extraCandies >= max_ele)
        
        return result