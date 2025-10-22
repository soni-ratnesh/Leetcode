class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        plots = 0
        right = (flowerbed).copy()

        for ii in range(1, len(flowerbed)):
            if flowerbed[ii] == 1:
                right[ii-1] = 1
                right[ii] = 1
        print(right)
        for ii in range(len(flowerbed)-2, -1, -1):
            if flowerbed[ii] == 1:
                right[ii+1] = 1
                right[ii] = 1

        print(right)
        count = 0
        ii=0
        while ii <(len(flowerbed)):
            if right[ii]==0:
                count+=1
                ii+=1
            ii+=1
        return count>=n

        
            
        return plots>=n