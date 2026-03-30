class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        # a dfs function inside subset so that we can have access to nums and others
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(sub.copy())
                return
            
            # on one side
            sub.append(nums[i])
            dfs(i + 1)

            # when we backtrack
            sub.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
        