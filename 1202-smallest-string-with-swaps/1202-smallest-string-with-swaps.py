class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        root= [ii for ii in range(len(s))]
        
        def find(x):
            if root[x] == x:
                return root[x]
            root[x] = find(root[x])
            return root[x]
        def union(x,y):
            root_x, root_y = find(x), find(y)

            if root_x!=root_y:
                root[root_y] = root[root_x]
            
        
        for x,y in pairs:
            union(x,y)
        print(root)
        
        d = {}
        d_index = {}
        for ii in range(len(s)):
            root_ii = find(ii)
            d.setdefault(root_ii, []).append(s[ii])
            d_index.setdefault(root_ii, []).append(ii)
        
 
        print(d)
        print(d_index)
        new_s = ["" for _ in range(len(s))]
        for key, val in d.items():
            val = sorted(val)
            jj=0
            for ii in d_index[key]:
                new_s[ii] = val[jj]
                jj+=1
        
        return "".join(new_s)
            
            
            