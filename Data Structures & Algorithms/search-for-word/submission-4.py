class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, i):
            # we keep increasing i and if it gets to the length of the word, then we found it
            if i == len(word):
                return True
            
            # backtrack
            if r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c] or (r,c) in path:
                return False
            
            # check ups and downs, we build paths because we can revit the space twice
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # if none return true
            path.remove((r, c))
            return res


        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False

        # we go throug board and from the board we check each of the directions.
