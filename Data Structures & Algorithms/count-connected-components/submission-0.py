class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # start from the first node
        # do a dfs until we're done with that node and all of its neighbors
        # exit dfs, increase the count of connected components
        # after we're done will all the nodes, just return the number
        adj = { i:[] for i in range(n) }
        components = 0
        # we're going to have a visited set to keep track of the things that we're visiting
        visited = set()
        
        # populate the adj list we just created for undirected graph
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            
            return
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        
        return components

        