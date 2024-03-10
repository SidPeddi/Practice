# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)
            return   
        ans = []
        dfs(root)
        return ans