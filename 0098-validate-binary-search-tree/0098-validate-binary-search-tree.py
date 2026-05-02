# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(root, min_limit, max_limit):
            if not root:
                return True
            
            if not min_limit<root.val<max_limit:
                return False
            
            return dfs(root.left, min_limit, root.val) and dfs(root.right, root.val, max_limit)            
        
        is_valid  = dfs(root, float("-inf"), float("inf"))
        
        return is_valid