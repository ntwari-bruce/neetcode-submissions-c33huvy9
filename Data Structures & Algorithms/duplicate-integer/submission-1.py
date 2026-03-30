class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # [2, 3, 3, 4]
        # immediate solution in mind
        # sort
        # if a single or no number, return false
        # loop through the input comparing two numbers
        # if they are the same, return true, else return false
        # time complexity: sort-> O(nlogn) + n
        # space complexity of O(n) for the additional array using by timsort

        # ===========
        # second approach
        # have a dictionary of each number and its count of occurences
        # loop through that, if the number's occurance is more than one return false
        # time complexity: O(n): looping throug the n values of the input
        # space complexity: O(n): dictionary store 

        # let me go ahead with the second solution

        # edge cases
        if not nums or len(nums) == 1:
            return False

        nums_count = dict()
        # if a number already exist in nums_count increase its occurence else start it as a key with 1
        for num in nums:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1
        
        for num, occurence in nums_count.items():
            if occurence > 1:
                return True
        
        return False


        
          
        