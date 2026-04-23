class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def dfs(i, curr):
            # base case
            if i == len(nums):
                subset.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i + 1, curr)

            # after backtracking
            curr.pop()
            dfs(i + 1, curr)
    
        dfs(0, [])

        return subset
                
        