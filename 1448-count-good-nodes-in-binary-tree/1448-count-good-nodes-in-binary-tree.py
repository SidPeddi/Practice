# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,root.val)

    
    
    
    def dfs(self,node, lastlargest):
        if not node:
            return 0
        if node.val >= lastlargest:
            res = 1
            lastlargest = node.val
        else:
            res = 0
        res += self.dfs(node.left, lastlargest)
        res += self.dfs(node.right, lastlargest)
        return res