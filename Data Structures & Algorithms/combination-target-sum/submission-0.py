class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, total):
            # base case if we find the total
            if total == target:
                res.append(subset.copy())
                return
            # base case 2, we go out of bounds
            if i >= len(nums) or total > target:
                return
            
            subset.append(nums[i])
            dfs(i, subset, total + nums[i])

            subset.pop()
            # we just gonna pass in total because we have removed the num[i]
            dfs(i + 1, subset, total)

        dfs(0, [], 0)
        return res