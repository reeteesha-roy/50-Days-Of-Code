class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        total = 0
        
        # Check if left child is a leaf
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        
        # Recursively sum left leaves in left and right subtrees
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        
        return total
