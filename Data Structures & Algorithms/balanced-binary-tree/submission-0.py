# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, curr):
        if not curr:
            return 0
        
        leftDepth = self.depth(curr.left)
        if leftDepth == -1:
            return -1
        rightDepth = self.depth(curr.right)
        if rightDepth == -1:
            return -1

        if abs(leftDepth - rightDepth) > 1:
            return -1

        return max(leftDepth, rightDepth) + 1

    def isBalanced(self, root) -> bool:
        return self.depth(root) != -1
        