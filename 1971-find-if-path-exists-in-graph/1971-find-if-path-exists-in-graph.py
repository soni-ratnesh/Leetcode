class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        
        for n1, n2 in edges:
            graph.setdefault(n1,[]).append(n2)
            graph.setdefault(n2,[]).append(n1)
        
        stack = [source]
        visited = set([source])
        while stack:
            node = stack.pop()
            
            
            if node == destination:
                return True
            
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    stack.append(n)
        
        return False
        