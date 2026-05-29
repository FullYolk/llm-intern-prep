# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.times = 0
        self.res = 0

        

        def dfs(root):
            if not root or self.times == k:
                return
            
            dfs(root.left)
            if self.times == k:
                return
            self.times = self.times+1
            if self.times == k:
                self.res = root.val
                return
            dfs(root.right)
    
        dfs(root)
        return self.res
