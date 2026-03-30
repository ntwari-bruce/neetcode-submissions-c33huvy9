# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # all the values from the top have to be less than the node.
        stack = [(root, float('-inf'))]
        # the counter #number of good nodes
        good_ones = 0
        while stack:
            node, largest = stack.pop()
            if largest <= node.val:
                good_ones += 1
            
            # update the largest value
            largest = max(largest, node.val)
            if node.left: stack.append((node.left,largest))
            if node.right: stack.append((node.right, largest))
        # we are returning the number of the good nodes
        # we are just making sure that we are only returning the amount of the good 
        # nodes in the equation
        return good_ones

        