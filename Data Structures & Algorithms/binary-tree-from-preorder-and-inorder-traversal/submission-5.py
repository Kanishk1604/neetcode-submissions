# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = {v: i for i, v in enumerate(inorder)}
        index = 0
        def dfs(l, r):
            nonlocal index
            if l > r:
                return None
            
            root_val = preorder[index]
            root = TreeNode(root_val)
            index_of_root = indexMap[root_val]
            index += 1

            root.left = dfs(l, index_of_root - 1)
            root.right = dfs(index_of_root + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)
