# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # this is a base case
        if not root:
            return 0
        
        # initalise a deque
        queue = deque([root])
        # initialise depth count
        depth = 0
        # iterate throught a deque
        while queue:
            # iterate thought the queue
            for i in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            # here after processing every level, we increase the depth by one
            depth += 1
        
        # after processing all the levels in a tree,
        return depth
        

        
        
        