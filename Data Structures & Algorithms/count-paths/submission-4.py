class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = {}
        def dfs(row, col):
            if row >= m or col >= n:
                return 0
            
            if row == (m - 1) and col == (n - 1):
                return 1
            
            if (row, col) in cache:
                return cache[(row, col)]
            
            cache[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)

            return cache[(row, col)]
        
        return dfs(0,0)