# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, float("inf"), float("-inf"))
    
    def valid(self, root, right , left):
        if not root:
            return True
        if not (left < root.val < right):
            return False
        
        return (self.valid(root.left, root.val, left) and self.valid(root.right, right, root.val))
