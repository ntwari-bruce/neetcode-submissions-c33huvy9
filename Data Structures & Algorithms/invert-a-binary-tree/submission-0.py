
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # this is how i am going to try to solve this problem with the use of recursion
        # start with a base case \
        if not root:
            return None
        # initalise a doube ended queue
        queue = deque([root])
        # iterate through this queue
        while queue:
            current = queue.popleft()
            # this is where we are going to swap
            current.left, current.right = current.right, current.left

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        # after the iteration we are just going to return the root

        return root
        
        