class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # the brute force solution
        # i can at step 0 or step one
        # can now optimize the 

        cache = [-1] * len(cost)
        def dfs(i):
            # base case, if we pass the top, we have no more cost to pay
            if i >= len(cost):
                return 0
            
            if cache[i] != -1:
                return cache[i]
            # pay this current cost plus the min from i + 1, i + 2
            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return cache[i]
        
        return min(dfs(0), dfs(1))
        
            