# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST property: left < root < right
        current = root

        while current:
            # If both p and q are greater, LCA must be in the right subtree
            if p.val > current.val and q.val > current.val:
                current = current.right
            # If both p and q are smaller, LCA must be in the left subtree
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                # Split point: one is on the left and one is on the right (or one is current)
                return current
