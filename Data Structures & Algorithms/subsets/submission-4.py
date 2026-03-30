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

        # time complextity
    #-------------------------
    # O(n * 2^n) for the input n we'll have 2 ^ n subset,
    # for each subset we are copying worst case n array moving it to the res

       # space complexity
    #--------------------------
    # O(n * 2^n) we'll store subset 2^n and and each subset can be of length n
    # the temporary list of O(n) and recursion stack is O(n) giving the overall 
    # O(n * 2^n)
        