class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # this is the brute force operation
        m , n = len(word1), len(word2)
        # adding caching to make it optimal
        cache = {}
        def dfs(i, j):
            # if we've exhausted all word1, add the remaining
            # characters from word2
            if i == m:
                return n - j
            # if we exhaust all word2, we delete the remaining characters
            # from word1
            if j == n:
                return m - i
            
            # if we've computed it, return it
            if (i, j) in cache:
                return cache[(i, j)]
            
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
            
            # if word1[i] !== word2[j]
            # we're going to have 3 options
            # dfs(i+1, j)   → deleted  'a' from word1     → only i moves
            # dfs(i, j+1)   → inserted 'c' into word1     → only j moves 
            # dfs(i+1, j+1) → replaced 'a' with 'c'       → BOTH move
            else:
                res = min(dfs(i + 1, j), dfs(i, j + 1))
                res = min(res, dfs(i + 1, j + 1))
                cache[(i, j)] = res + 1
            # return 1( current operation) plus res future operation
            # return res + 1
            return cache[(i, j)]
        return dfs(0,0)


        # time complexity is O(m * n) possible m * n (i, j)
        # space complexity O(m * n) caching and callback