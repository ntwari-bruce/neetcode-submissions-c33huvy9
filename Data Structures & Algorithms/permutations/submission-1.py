class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # start with an empty perm [[]]
        # while iterating through the numbers, add the number to the available perm, and position
        # add each number to each position in a permutation

        perms = [[]]
        for num in nums:
            new_perm = []
            for p in perms:
                # iterate through that perm to add the number on each of the position
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perm.append(p_copy)
            perms = new_perm
        
        return perms
            
         # time complexity O(n^2 * n!)
         #--------------------------------
        # we have O(n) copies, O(n) shifting operations 
        # we generate n! total permutations

        # space complexity O(n * n!)
        #-----------------------------------
        # storing final results contains total n! permutation
        # each individual permutatation is on list n size
        # []  
        # [1]  
        # [1,2], [2,1]  
        # [1,2,3], [2,1,3], [2,3,1], ...