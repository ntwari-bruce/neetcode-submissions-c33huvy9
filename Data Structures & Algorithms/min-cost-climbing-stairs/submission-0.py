class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Say we have array 
        # [10, 15, 20]
        # we'll add a 0 [10, 15, 20, 0] because reaching this 0 means at the top
        # we start at 15 because that is where we can make 2 jumps or one jump
        # we can jump from 15 to 20 and from 20 to 0 , and we can jump from 15 to zero.
        # jumping from 15 to 0( two steps ) might look like the best way now but later they can be a bigger value there

        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        
        # because we can either start from 0, 1, we're going to return the minimum of those
        # we're guaranteed two values in the array
        return min(cost[0], cost[1]) 