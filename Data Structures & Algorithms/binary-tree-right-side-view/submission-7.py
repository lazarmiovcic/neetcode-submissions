# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([(root, 0)])
        depths = {}
        while q:
            node, lvl = q.popleft()
            if not lvl in depths:
                depths[lvl] = node
            
            if node.right:
                q.append((node.right, lvl + 1))
            if node.left:
                q.append((node.left, lvl + 1))
        
        return [node.val for node in depths.values()]
