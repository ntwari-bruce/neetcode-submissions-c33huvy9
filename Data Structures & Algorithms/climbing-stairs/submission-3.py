class Solution:
    def climbStairs(self, n: int) -> int:
        # the approach is to start and end, using 
        # these two available ones

        # brute force solution
        
        # improving the solution by cashing to reduce the repeated wordd
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)

            return cache[i]
        
        return dfs(0)

        # on each i we are making two decisions
        # Time complexity O(2^n)

        # Space complexity
        # the recursion depth is of the size n
        # overall space complexity is O(n)
        