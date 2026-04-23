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

# for every index we make two decision and we have total n (2^n)
# when we hit the base case, we do curr.copy() which takes O(n)
# time is O(n * 2^n)

# the subset stores up to 2^n subsets, and worst case each is up to n
# resulting in O(n * 2^n)
# the O(n) for stack, the recursion goes n levels deep until we hit
# the base case

# the space complexity is O(n * 2^n)
        
                
        