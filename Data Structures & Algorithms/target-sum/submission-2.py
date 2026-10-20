class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, current_sum):

            if (i, current_sum) in cache:
                return cache[(i, current_sum)]

            if i == len(nums):
                return 1 if current_sum == target else 0

            left = dfs(i + 1, current_sum + nums[i])

            right = dfs(i + 1, current_sum - nums[i])

            cache[(i, current_sum)] = left + right
            return left + right
        
        return dfs(0, 0)


        