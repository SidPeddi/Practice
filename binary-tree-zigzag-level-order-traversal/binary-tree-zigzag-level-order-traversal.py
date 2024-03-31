# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        left = 0
        
        while queue:
            current_length = len(queue)
            temp = []
            if left:
                left = 0
            else:
                left = 1
            
            for _ in range(current_length):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if left:
                ans.append(temp)
            else:
                ans.append(temp[::-1])
        
        return ans