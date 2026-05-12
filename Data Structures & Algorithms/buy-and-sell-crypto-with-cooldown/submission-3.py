# Optimised code.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if we're cooling down, we're skipping that
        cache = {}

        def dfs(i, buying):
            if (i, buying) in cache:
                return cache[(i, buying)]

            if i >= len(prices):
                return 0
            
            # define cool down, we skip current, and keep buying option open
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cache[(i, buying)] = max(buy, cooldown)
                return max(buy, cooldown)
            else:
                # we're skipping a day
                sell = dfs(i + 2, not buying) + prices[i]
                cache[(i, buying)] = max(sell, cooldown)
                return max(sell, cooldown)
        
        return dfs(0, True)
        
        # the unoptimised stock has O(2^n)
        # space of O(n) for the recursion stack.