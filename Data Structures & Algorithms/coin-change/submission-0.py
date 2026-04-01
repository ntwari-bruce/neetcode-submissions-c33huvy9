class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Think of it like this.
        # coints [1,2] and amount is 3
        # we create [4,4,4]
        # iterate through each coin comparing dp[i], and 1 + dp[a - c]
        # 1 is if we use that specific coint and dp[a - c] is for what we have computed earlier
        dp = [amount + 1] * (amount + 1) # from 0 to amount
        # we take 0 coin to make amount 0
        dp[0] = 0

        #iterate through the dp, checking each coin
        #Remember a is the index not dp[a] value
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        # 
        return dp[amount] if dp[amount] != amount + 1 else -1 
        
        # time complexit O(coins * amount)
        # space O(amount)
        