class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area_of_island = 0
        max_area = 0
        # dfs to recursively count the area of island
        def dfs(r, c):
            # check the boundaries and visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            # mark the island visited by turning it to 1
            grid[r][c] = 0

            return 1 + dfs(r, c - 1) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r + 1, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area_of_island = dfs(r, c)
                    max_area = max(max_area, area_of_island)
        
        return max_area

        