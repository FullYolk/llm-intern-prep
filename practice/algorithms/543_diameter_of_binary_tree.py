# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.max_depth
    
    def depth(self,root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)

        if (left + right) > self.max_depth:
            self.max_depth = left + right

        return max(left,right) + 1 
        
        