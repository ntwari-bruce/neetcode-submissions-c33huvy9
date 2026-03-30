# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # validate 
        def valid(node, min_, max_):
            if not node:
                return True
            if node.val >= max_ or node.val <= min_:
                return False
            return valid(node.left, min_, node.val) and valid(node.right, node.val, max_)
        return valid(root, float('-inf'), float('inf'))
        
        



        