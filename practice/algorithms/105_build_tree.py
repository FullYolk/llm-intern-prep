# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        mid_idx = inorder.index(root_val)
        left_inorder = inorder[:mid_idx]
        right_inorder = inorder[mid_idx+1 :]
        len_left = len(left_inorder)
        preorder_left = preorder[1:1+len_left]
        preorder_right = preorder[1+len_left:]
        root.left = self.buildTree(preorder_left,left_inorder)
        root.right = self.buildTree(preorder_right,right_inorder)
        return root
    
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i,val in enumerate(inorder):
            inorder_map[val] = i
        
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            mid_idx = inorder_map[root_val]

            left_len = mid_idx - in_start

            root.left = build(pre_start + 1, pre_start + left_len, in_start, mid_idx - 1)
            root.right = build(pre_start + left_len + 1, pre_end, mid_idx + 1, in_end)

            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)