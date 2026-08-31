class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case, if we're out of bounds, return 0
        # or if we reach the end of the array
        # optimization
        cache = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]

            cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return cache[i]
        
        return dfs(0)



        
