class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # we are going to iterate with two pointers
        # if we hve matching chars in both texts, we move pointers
        # simultaneously
        # else, we move right -> while stopping left or vice virce, and # return the maximum
        
        # we optimise time and space complexity through caching
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            # base case
            if i == len(text1) or j == len(text2):
                return 0
            
            # if characters are equal, we return one
            if text1[i] == text2[j]:
                res = 1 + dfs(i + 1, j + 1)
                cache[(i, j)] = res
            
            # here if characters are not equal, we return the maximum
            else:
                res = max(dfs(i + 1, j), dfs(i, j + 1))
                cache[(i, j)] = res
            
            return res

        return dfs(0, 0)

        # worst case time complexity O(2^ m + n)
        # space is the dfs recursion stack of O(m + n)

