"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            
            new_node = Node(val=node.val)
            visited[node] = new_node
            neighbors = []
            for n in node.neighbors:
                neighbors.append(dfs(n))
            new_node.neighbors = neighbors
            return new_node
        
        return dfs(node) if node else None
            