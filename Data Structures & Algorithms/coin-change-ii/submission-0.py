class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        cache = {}
        def dfs(i, a):
            if (i, a) in cache:
                return cache[(i, a)]
            # base case1
            # Meaning we have made up to that amount
            if a == 0:
                return 1
            # if we reach the end of the length
            # meaning we reached the end, return zero
            if i >= len(coins):
                return 0
            
            # Meaning here we can still use the coin
            res = 0
            if a >= coins[i]:
                res = dfs(i, a - coins[i])
                res += dfs(i + 1, a)
            
            cache[(i, a)] = res
            return res

        return dfs(0, amount)    
           
        