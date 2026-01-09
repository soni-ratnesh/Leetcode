class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(ii, jj):
            visited[ii][jj]=1

            moves = [[0,1],[0,-1],[-1,0],[1,0]]

            for d_ii, d_jj in moves:
                new_ii, new_jj = ii+d_ii, jj+d_jj
                print(new_ii, new_jj,in_range(new_ii, new_jj) )
                if in_range(new_ii, new_jj) and visited[new_ii][new_jj] ==0 and grid[new_ii][new_jj]=="1":
                    dfs(new_ii, new_jj)

        def in_range(ii, jj):
            return 0<=ii<len(grid) and 0<=jj<len(grid[0])

        m,n = len(grid), len(grid[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]
        count = 0
        for ii in range(m):
            for jj in range(n):
                if (visited[ii][jj]==0) and (grid[ii][jj]=="1"):
                    count+=1
                    dfs(ii,jj)
                
        return count