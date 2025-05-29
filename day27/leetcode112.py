class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        # If it's a leaf node
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recurse on the left and right children
        remainingSum = targetSum - root.val
        return (self.hasPathSum(root.left, remainingSum) or
                self.hasPathSum(root.right, remainingSum))
