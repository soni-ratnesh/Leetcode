class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ii, jj = 0, len(matrix[0])-1

        while 0<=ii<len(matrix) and 0<=jj<len(matrix[0]):
            if target == matrix[ii][jj]:
                return True
            elif target < matrix[ii][jj]:
                jj-=1
            else:
                ii+=1
        return False