class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def dfs(i, j):

            if (i, j) in cache:
                return cache[(i, j)]

            # reach end word1, insert all of word2
            if i == len(word1):
                return len(word2) - j
            
            # reach the end or word2, delete the rest of word1
            # i meaning that's where we were before reaching the end
            if j == len(word2):
                return len(word1) - i
            
            # if both chars in word1 and word2 aligns, no operation, just move on
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            # otherwise
            # delete, insert, replace
            res = min(1 + dfs(i + 1, j) , 1 + dfs(i, j + 1), 1 + dfs(i + 1, j + 1) )
            cache[(i, j)] = res
            return res
        return dfs(0, 0)