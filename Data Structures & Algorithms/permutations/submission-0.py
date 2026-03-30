class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            new_perm = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    # we're adding the number in every position
                    p_copy.insert(i, num)
                    new_perm.append(p_copy)

            perms = new_perm
        
        return perms
        # time complexity O(n^2 * n!)
        # we have O(n) copies, O(n) shifting operations 
        # we generate n! total permutations

        # space complexity O(n * n!)
        # storing final results contains total n! permutation
        # each individual permutatation is on list n size
        