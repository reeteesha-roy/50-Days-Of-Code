class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        def helper(node):
            nonlocal prev
            if not node:
                return
            # Go right first because we are building from end to start
            helper(node.right)
            helper(node.left)

            node.right = prev
            node.left = None
            prev = node

        prev = None
        helper(root)

