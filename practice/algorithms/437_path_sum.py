# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        res = self.root_sum(root,targetSum)

        res = res + self.pathSum(root.left,targetSum)

        res = res + self.pathSum(root.right,targetSum)
        
        return res

    def root_sum(self,node,target):
        if not node:
            return 0
        count = 0
        if node.val == target:
            count = count + 1
        left = self.root_sum(node.left, target - node.val)
        right = self.root_sum(node.right,target - node.val)
        return count + left + right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_map = {0:1}

        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum = curr_sum + node.val

            count = prefix_map.get(curr_sum - targetSum, 0)

            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right,curr_sum)

            prefix_map[curr_sum] -= 1
            return count
        
        return dfs(root, 0)