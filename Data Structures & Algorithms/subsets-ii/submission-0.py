class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                # this is to control the duplicates
                if subset not in res:
                    res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            # on other side
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

        