class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''we're making a decision at every step, include or skip due to the condition, initially the out of bounds index is equal to the negative number'''
        cache = {}
        def dfs(i, j):
            # base case, if we reach the down-end
            # return 0
            if i == len(nums):
                return 0
            
            if (i,j) in cache:
                return cache[(i, j)]
            # Here we skip
            LIS = dfs(i + 1, j)
            cache[(i,j)] = LIS

            # on the backtracking side
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))
                cache[(i,j)] = LIS
            
            return LIS
        
        return dfs(0, -1)

        
            
        