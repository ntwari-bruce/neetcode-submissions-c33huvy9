class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path:
                return False
                
            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        # if we finish the whole letter and no match return false
        return False


        # time complexity
        # the outer loop goes through each row * col
        # m = row * col
        # from each m we try 4 directions
        # L is the length of the word

        # Total time complexity if O(m * 4^L)


        # for space we're keeping two things
        # The path (r, c) and the recursion stack
        # at most path will hold L cells long
        # O(L)

        # The recursion will go as deep as L
        # Total time complexity O(L)
        