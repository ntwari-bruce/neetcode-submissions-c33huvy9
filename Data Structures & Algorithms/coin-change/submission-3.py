class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        def dfs(amount):
            if amount in cache:
                return cache[amount]

            # base case
            if amount == 0:
                return 0
            
            res = float("inf")

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            cache[amount] = res
            return res
        
        minCoins = dfs(amount)

        return -1 if minCoins >= float("inf") else minCoins


        # this brings the time complexity from O(2^n) to O(n)
        # this eases the time complexity way hard. 