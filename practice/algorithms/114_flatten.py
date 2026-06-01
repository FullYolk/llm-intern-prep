# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr is not None:
            if curr.left:
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right

#右子树接到左子树的最右节点 然后左子树变成右子树 继续遍历