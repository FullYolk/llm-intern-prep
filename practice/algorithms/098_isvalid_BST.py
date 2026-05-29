# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre_val = float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left:
            left = self.isValidBST(root.left)
        else:
            left = True
        if root.val <= self.pre_val:
            return False
        self.pre_val = root.val
        if root.right:
            right = self.isValidBST(root.right)
        else:
            right = True
        if left and right:
            return True
        return False
  #更好的写法:      
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 在每次调用主函数时，初始化实例变量，绝对安全
        self.pre_val = float('-inf')
        
        # 定义一个专门用来递归的辅助函数
        def inorder(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            
            # 1. 查左子树，如果左边不合法，直接返回 False (剪枝加速)
            if not inorder(node.left):
                return False
            
            # 2. 查根节点
            if node.val <= self.pre_val:
                return False
            self.pre_val = node.val # 更新上一个访问的值
            
            # 3. 查右子树
            return inorder(node.right)
            
        return inorder(root)
