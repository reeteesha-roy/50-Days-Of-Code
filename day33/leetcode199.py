class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                
                # If it's the last node of this level, it's visible from the right
                if i == level_size - 1:
                    result.append(node.val)

                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

