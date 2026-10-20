class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        def dfs(i, j, k):
            if (i, j, k) in cache:
                return cache[(i, j, k)]

            if k == len(s3):
                return True if i == len(s1) and j == len(s2) else False
            
            if i < len(s1) and s3[k] == s1[i]:
                if dfs(i + 1, j, k + 1):
                    cache[(i, j, k)] = True
                    return True
            
            if j < len(s2) and s3[k] == s2[j]:
                if dfs(i, j + 1, k + 1):
                    cache[(i, j, k)] = True
                    return True

            cache[(i, j, k)] = False
            return False
        
        return dfs(0, 0, 0)