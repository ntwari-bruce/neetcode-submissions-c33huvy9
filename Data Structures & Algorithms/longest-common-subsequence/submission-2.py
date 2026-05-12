class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if we have a return means that the function is just 
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            # If we reach either of the lengths
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                # cache the results
                cache[(i, j)] = 1 + dfs(i + 1, j + 1)
                return 1 + dfs(i + 1, j + 1)
            
            cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return max(dfs(i + 1, j), dfs(i, j + 1))
        
        return dfs(0,0)

# time complexity after optimization is O(mxn)
# the cache stores results of (i, j) and there are mxn pairs
# space complexity is O(mxn)
        