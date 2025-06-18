class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        # Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found - now delete it
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Node has two children
                # Find the inorder successor (smallest in right subtree)
                successor = self.findMin(root.right)
                # Copy the successor's value
                root.val = successor.val
                # Delete the successor
                root.right = self.deleteNode(root.right, successor.val)
        
        return root
    
    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
