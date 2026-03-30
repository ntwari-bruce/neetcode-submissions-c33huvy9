class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # this is a backtracking question
        res = []
        subset = []

        def dfs(i):
            # the base case for backtracking
            if i >= len(nums):
                # here we're editing the subset so we taking the copy 
                # so that the modifications doesn't affect it
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            # on the right side
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res