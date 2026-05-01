class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        def dfs(i, curr_total):
            if curr_total == target:
                return True
            if i >= len(nums) or curr_total > target:
                return False
            
            # don't skip a number
            if dfs(i + 1, curr_total + nums[i]):
                return True
            
            # skip a number, this
            if dfs(i + 1, curr_total):
                return True
            
            return False
        return dfs(0, 0)


        