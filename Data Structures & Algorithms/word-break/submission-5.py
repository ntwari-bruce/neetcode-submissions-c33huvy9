class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return True
            
            for j in range(i, len(s)):
                if s[i: j + 1] in wordSet:
                    if dfs(j + 1):
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False

        return dfs(0)

        # the time complexity becomes O(n^3)