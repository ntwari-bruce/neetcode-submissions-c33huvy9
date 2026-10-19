class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # we go down the dfs tracking the current index and total
        # amount
        coins.sort()
        cache = {}
        def dfs(i, current):
            if (i, current) in cache:
                return cache[(i, current)]
            # if current is 0 means means we have used up that coin
            if current == 0:
                return 1
            
            # if we reach the end, return 0
            if i >= len(coins):
                return 0
            
            left, right = 0, 0
            # if the current amount can make up to that coin
            if current >= coins[i]:
                left = dfs(i, current - coins[i])
                # after getting the results here, we reached zero or the end or didn't make up to that amount, we go to the next coin
                # we pass in current, we move to the next side of the tree, still pass in what we had at this level
                right = dfs(i + 1, current)
            cache[(i, current)] = left + right
            return left + right
        
        return dfs(0, amount)


        