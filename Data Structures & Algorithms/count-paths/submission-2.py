class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # for caching the results
        cache = {}
        # finding the unique paths
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            # if we reach the goal, return 1
            if i == (m - 1) and j == (n - 1):
                return 1
            
            # if we go out of bounds, because we're only
            # moving to the right, and down
            if i >= m or j >= n:
                return 0
            
            path = dfs(i, j + 1) + dfs(i + 1, j)
            cache[(i, j)] = path

            return path
        
        return dfs(0, 0)


        # Time complexity before optimization O(2 ^ (m + n))
        # space complexity before optimization O(m + n)

        # Time complexity after optimization O(m x n)
        # Cache stores results O(m x n)
        