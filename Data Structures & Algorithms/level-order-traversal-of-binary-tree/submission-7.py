# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = deque([(root, 0)])
        depths = {0: [root.val]}
        while q:
            node, level = q.popleft()
            
            if node.left:
                q.append((node.left, level+1))
                if level + 1 in depths:
                    depths[level+1].append(node.left.val)
                else:
                    depths[level+1] = [node.left.val]
            
            if node.right:
                q.append((node.right, level+1))
                if level + 1 in depths:
                    depths[level+1].append(node.right.val)
                else:
                    depths[level+1] = [node.right.val]
        
        return [l for l in depths.values()]