# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node, mini, maxi):
            if not node:
                return maxi - mini
            return max(dfs(node.left,min(mini,node.val),maxi = max(maxi,node.val)), dfs(node.right ,min(mini,node.val),maxi = max(maxi,node.val)))
        
        
        return dfs(root, root.val, root.val)
        