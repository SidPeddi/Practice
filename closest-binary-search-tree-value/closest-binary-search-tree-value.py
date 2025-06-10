# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            if (abs(target - node.val) < minval[0]) or (abs(target - node.val) == minval[0] and node.val < ans[0]):
                minval[0] = abs(target - node.val)
                ans[0] = node.val                
            right = dfs(node.right)
        ans = [root.val]
        minval = [float("inf")]
        dfs(root)
        return ans[0]
        