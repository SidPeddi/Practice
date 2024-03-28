# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, node, tSum, targetSum):
        if not node:
            return False
        
        if not node.left and not node.right and (tSum + node.val) == targetSum:
            return True
        tSum += node.val
        return self.dfs(node.left, tSum, targetSum) or         self.dfs(node.right, tSum, targetSum)


    
    
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, 0, targetSum)
