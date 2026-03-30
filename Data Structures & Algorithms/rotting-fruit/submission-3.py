class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        minutes = 0

        # count the number of fresh fruit and ropistions for rotten ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    if dr + r < 0 or dr + r >= ROWS or dc + c < 0 or dc + c >= COLS or grid[dr + r][dc + c] != 1:
                        continue
                    grid[dr + r][dc + c] = 2
                    queue.append([dr + r, dc + c])
                    # we reduce the number of fresh fruits 
                    fresh -= 1
            # increase the number of minutes
            minutes += 1
        
        # we return the time when fresh_fruit is 0 or else -1( meaning we have exhuasted all the fresh fruits)
        return minutes if fresh == 0 else -1


        
                

        