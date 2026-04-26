class Solution:
    DIRECTIONS = [(0,1), (0,-1),(-1,0),(1,0)]
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        # count 
        n_islands = 0
        rows, cols = len(grid), len(grid[0])

        # function to check if its inbounds
        def inbounds(row, col):
            return 0<=row<rows and 0<=col<cols
        # dfs 
        def dfs(row, col):
            stack = [(row,col)]

            while stack:
                r,c = stack.pop()
                
                if not inbounds(r,c) or grid[r][c] == "0":
                    continue
                
                grid[r][c] = "0"

                for dr, dc in self.DIRECTIONS:
                    nr, nc = r+dr, c+dc
                    stack.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    n_islands+=1
                    dfs(r,c)
        
        return n_islands