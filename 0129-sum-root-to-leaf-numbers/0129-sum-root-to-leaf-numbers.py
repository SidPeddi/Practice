# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        self.dfs(root, 0, ans)
        return sum(ans)
            
    def dfs(self, node, tSum, ans):
        if not node:
            return
        tSum += node.val
        if not node.left and not node.right:
            ans.append(tSum)
        tSum *= 10
        
        return self.dfs(node.left, tSum, ans) or self.dfs(node.right, tSum, ans)