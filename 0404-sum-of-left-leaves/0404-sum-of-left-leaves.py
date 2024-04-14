# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node, isleft):
            if not node:
                return 0
            if not node.left and not node.right and isleft:
                return node.val
            leftsum = dfs(node.left, True) 
            rightsum = dfs(node.right, False)
            return leftsum + rightsum

        return dfs(root, False)
        