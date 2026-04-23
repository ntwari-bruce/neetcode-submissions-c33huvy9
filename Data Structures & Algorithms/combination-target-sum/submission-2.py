class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        def dfs(i, curr, curr_sum):
            # base case 1
            if i == len(nums) or curr_sum > target:
                return
            
            if curr_sum == target:
                combinations.append(curr.copy())
                return 
            
            curr.append(nums[i])
            dfs(i, curr, curr_sum + nums[i])

            # when we backtrack(coming on other side of the tree)
            curr.pop()
            dfs(i + 1, curr, curr_sum) # remember we're backtracking so we'll have the total that we had and the array that we had
        
        dfs(0, [], 0)
        return combinations
        
# time complexity 
# we're making 2 decisions per each item
# worst case the tree can grow to target/ minimum item O(2^ t/m)

# time complexity:
# the recursion height in worst case in target/minimum item. 
# say target is 4 and we have [1] add 1 = [1,1], add 1 = [1,1,1]
# O(t/m)
        