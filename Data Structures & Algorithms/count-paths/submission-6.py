class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # we start from the corner grid[0][0]
        # we take paths from the right,and move down
        # then have their sum
        cache = {}

        def dfs(i, j):

            if (i, j) in cache:
                return cache[(i, j)]
            # base case
            if i == (m - 1) and j == (n - 1):
                return 1
            
            # return we get out of bounds, return 0
            if i >= m or j >= n:
                return 0
            
            # move right
            right = dfs(i, j + 1)
            # move down
            down = dfs(i + 1, j)

            cache[(i, j)] = right + down
            return right + down
        
        return dfs(0, 0)

        # on each cell we make two decision which grows with the number of rows and columns
        # The recursion depth is the size of O(m + n)

        # for the recursion stack count the moves that we're making.