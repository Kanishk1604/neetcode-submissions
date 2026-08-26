# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_inorder = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0
        def dfs(l, r):
            nonlocal pre_idx
            if l > r:
                return
            
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            mid = index_inorder[root_val]
            pre_idx += 1
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        return dfs(0, len(inorder) - 1)