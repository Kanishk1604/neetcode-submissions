# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, value):
            nonlocal count
            if not node:
                return 
            
            if node.val >= value:
                value = node.val
                count += 1
            
            dfs(node.left, value)
            dfs(node.right, value)
        
        dfs(root, float("-inf"))

        return count
