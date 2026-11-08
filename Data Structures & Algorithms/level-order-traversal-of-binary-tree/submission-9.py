# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depths = {}
        def dfs(node, depth):
            nonlocal depths
            if not node:
                return None
            
            if len(depths) == depth:
                depths[depth] = [node.val]
            else:
                depths[depth].append(node.val)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return [l for l in depths.values()]
