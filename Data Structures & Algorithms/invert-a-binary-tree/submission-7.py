# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # if we would assign inverted right to root.left we are changing root.left then we wood be passing that inverted tree to root.right

        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        
        root.left = right_inverted
        root.right = left_inverted
        
        return root

