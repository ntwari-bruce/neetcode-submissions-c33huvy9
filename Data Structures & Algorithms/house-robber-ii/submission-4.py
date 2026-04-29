class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(i, num, cache):
            if i >= len(num):
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(dfs(i + 1, num, cache), num[i] + dfs(i + 2, num, cache))
            return cache[i]
        
        cache1 = [-1] * len(nums)
        cache2 = [-1] * len(nums)
        return max(dfs(0, nums[1:], cache1), dfs(0, nums[:-1], cache2))
            

