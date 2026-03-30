class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                # we want to make this such that when we
                # modify the subset, the effect doesn't reflect in res's saved
                res.append(subset.copy())
                return
            
            # Include the num[i]
            subset.append(nums[i])
            dfs(i + 1)

            # do not include the num[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
        
        