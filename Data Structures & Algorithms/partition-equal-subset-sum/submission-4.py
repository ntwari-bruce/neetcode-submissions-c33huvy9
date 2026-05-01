class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        cache = {}
        def dfs(i, curr_total):
            if (i, curr_total) in cache:
                return cache[(i, curr_total)]

            if curr_total == target:
                cache[(i, curr_total)] = True
                return True
            if i >= len(nums) or curr_total > target:
                cache[(i, curr_total)] = False
                return False
            
            # don't skip a number
            if dfs(i + 1, curr_total + nums[i]):
                cache[(i, curr_total)] = False
                return True
            
            # skip a number, this
            if dfs(i + 1, curr_total):
                cache[(i, curr_total)] = False
                return True
            
            return False
        return dfs(0, 0)

# time complexity O(2^n)
# space complexity O(n) recursion stack
        