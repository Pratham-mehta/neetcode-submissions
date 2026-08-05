# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Diameter = height of left subtree + height of right subtree

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def height(root):
            nonlocal diameter
            if root is None:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            diameter = max(diameter, left_height + right_height)

            return 1+max(left_height, right_height)
        
        height(root)
        return diameter



