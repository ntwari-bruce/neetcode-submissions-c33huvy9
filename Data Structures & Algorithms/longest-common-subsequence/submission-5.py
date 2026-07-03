class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            # if we ever reach the length of any of these
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                result = 1 + dfs(i + 1, j + 1)
            else:
                result = max(dfs(i + 1, j), dfs(i, j + 1))
            
            cache[(i, j)] = result
            return result
        
        return dfs(0,0)
       


        