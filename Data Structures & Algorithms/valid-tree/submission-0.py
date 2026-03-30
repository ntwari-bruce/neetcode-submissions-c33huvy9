class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # according to the definition
        # a tree is an undirected graph with no cycle
        # in this problem we need to see if we detect a cycle
        adjMatrix= [ [0] * n for _ in range(n) ]

        if len(edges) != n - 1:
            return False
        # this is an undirected graph
        for u, v in edges:
            adjMatrix[u][v] = 1
            adjMatrix[v][u] = 1
        
        def dfs(v, visited, parent):
            # mark the vertex as fisited
            visited[v] = True
            for i in range(n):
                if adjMatrix[v][i] == 1:
                    if not visited[i]:
                        if not dfs(i, visited, v):
                            return False
                    elif parent != i:  # here meaning if we've visited this and it's not a parent, return False
                        return False
            return True # the recursion needs a return value

        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                if not dfs(i, visited, -1):
                    return False
        # check if it is a disconnected graph

        return True # if we didn't find any cycle, means that the tree is gucci
        
        
        
        

        