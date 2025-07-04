class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            # update diameter at this node
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # return height of this node
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.max_diameter
