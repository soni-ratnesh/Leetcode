class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(source, target):
            if source == target:
                return 1 
            
            for n in graph[source]:
                node, val = n
                if node not in visited:
                    visited.add(node)
                    r = dfs(node, target)
                    if r>0:
                        return r*val
            return -1

        graph = {}
        for ii in range(len(equations)):
            a,b = equations[ii]
            v = values[ii]

            graph.setdefault(a, []).append([b,v])
            graph.setdefault(b, []).append([a,1/v])
        
        result = []
        for ii in range(len(queries)):
            c,d = queries[ii]

            if c in graph and d in graph:
                visited = set()
                result.append(dfs(source=c,target=d))
            else:
                result.append(-1)
        return result

        