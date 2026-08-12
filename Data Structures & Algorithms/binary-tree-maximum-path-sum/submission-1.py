# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        resmax = root.val
        def dfs(node):
            nonlocal resmax
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            resmax = max(resmax, max(0,left) + max(0, right) + node.val)
            return max(0, node.val + max(0, max(left, right)))
        dfs(root)
        return resmax

        # 15
        #10 20

        #resmax
        #10
        #20
        # 20 vs 10 + 20 + (-15)
