class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        # dfs 
        def dfs(i):
            if i in cache:
                return cache[i]
            # base case 1
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)

            # here we're checking two digits options
            # meaning to if we can take two digits
            if i < len(s) - 1:
                if s[i] == "1" or s[i] == "2" and s[i + 1] < "7":
                    res += dfs(i + 2)
            
            cache[i] = res
            return res
        
        return dfs(0)


       