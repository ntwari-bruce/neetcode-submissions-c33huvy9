class Solution:
    def rob(self, nums: List[int]) -> int:
        # we start robbing skipping the first house entirely
        # start with the first and ignore the last house
        if len(nums) == 1:
            return nums[0]
        def dfs(i, nums, cache):
            # base case 1, if we're out, return 0
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]

            cache[i] = max(dfs(i + 1, nums, cache), nums[i] + dfs(i + 2, nums, cache))

            return cache[i]

        cache1 = [-1] * len(nums)
        cache2 = [-1] * len(nums)
        return max(dfs(0, nums[1:], cache1), dfs(0, nums[:-1], cache2))


