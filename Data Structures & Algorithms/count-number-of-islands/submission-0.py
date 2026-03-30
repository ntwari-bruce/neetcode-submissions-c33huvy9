class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # solution using breadth first search
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        Rows = len(grid)
        Columns = len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque()
            # here we are making it as visited
            grid[r][c] = "0"
            queue.append((r,c))

            while queue:
                row , col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nc < 0 or nr < 0 or nr >= Rows or nc >= Columns or  grid[nr][nc] == "0"):
                        continue

                    queue.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands
        