class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(root, x, y):
            root_x, root_y = find(x), find(y)
            if root_y != root_x:
                root[root_y] = root[root_x]
        
        
        root = [i for i in range(len(isConnected))]
            
        for ii in range(len(isConnected)):
            for jj in range(len(isConnected)):
                if isConnected[ii][jj] == 1:
                    union(root, ii,jj)
        for ii in range(len(root)):
            find(ii)
        return len(set(root))
                    
        
        