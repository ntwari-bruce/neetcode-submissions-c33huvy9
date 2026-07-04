class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i, buying):
            if (i, buying) in cache:
                return cache[(i, buying)]
            # if we are the end, no more prices to buy or sell
            if i >= len(prices):
                return 0
            
            # cooldown is we skip a day, but we're buying next
            coolDown = dfs(i + 1, buying)
            # if we're buying, we take that price
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cache[(i, buying)]=max(coolDown, buy)
                return cache[(i, buying)]
            else:
                # if we're selling, we can buy next
                sell = dfs(i + 2, not buying) + prices[i]
                cache[(i, buying)] = max(coolDown, sell)
                return cache[(i, buying)]
        
        return dfs(0, True)

        # we compare with cooldown because do nothing today
        # is always a legal move
            
      