class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}

        def dfs(amount):

            if amount == 0:
                return 0

            # we start by setting the result for the highest possible number
            res = float("inf")

            if amount in cache:
                return cache[amount]

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
                    cache[amount] = res
            

            return res
        
        final = dfs(amount)

        return -1 if final == float("inf") else final