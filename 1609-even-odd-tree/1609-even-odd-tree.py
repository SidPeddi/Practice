class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        even = 1
        queue = deque([root])
        while queue:
            nodes = len(queue)
            prev = -inf if even else inf
            for _ in range(nodes):
                node = queue.popleft()
                if even and(node.val % 2 == 0 or prev >= node.val):
                    return False
                elif not even and(node.val % 2 == 1 or node.val >= prev):
                    return False
                prev = node.val 
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            even ^= 1
        return True 
                        