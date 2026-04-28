class Solution:
    def rob(self, nums: List[int]) -> int:
        # when thinking through these dynamic programing questions,
        # just evaluate the first few initial steps and build upon them
        # we optimise the solution by caching
        cache = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0

            if cache[i] != -1:
                return cache[i]
            # we can choose to rob the first + third, or rob the second
            cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return cache[i]
        
        return dfs(0)


